#!/usr/bin/env python3
# use this command to run the script:
# python main-script.py --model furiosa-ai/Llama-3.3-70B-Instruct  --base-url http://localhost:8080/v1
# or python main-script.py --model gpt-4o-mini --base-url https://api.openai.com/v1
# or python main-script.py --model meta-llama/Meta-Llama-3-70B-Instruct  --base-url http://localhost:8000/v1

"""
Automated Faceting and Filtering with Elasticsearch and OpenAI

This script demonstrates:
1. Generating synthetic personal profile data
2. Uploading data to Elasticsearch
3. Using OpenAI to convert natural language to Elasticsearch queries
4. Executing automated searches

Before running, ensure you have:
- Elasticsearch endpoint and API key in .env
- OpenAI API key in .env
- Required Python packages installed
"""


import traceback
import uuid
import os
from elasticsearch import Elasticsearch, helpers

from openai import OpenAI
from dotenv import load_dotenv
import json
import random
from datetime import datetime, timedelta
import string
from pprint import pprint
import logging

import pickle
import argparse
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.disable(logging.CRITICAL)

from gen_employees_data import generate_employee_profiles


print_search_results = False

prompt='''
You are an AI assistant specialized in converting natural language queries into Elasticsearch queries. 
Your task is to interpret user questions about personal profiles and generate the appropriate Elasticsearch query in JSON format.

The document schema for the profiles is as follows:

{
        "id": 1,
        "name": "Huntlee Dargavel",
        "email": "hdargavel0@japanpost.jp",
        "gender": "male",
        "ip_address": "58.11.89.193",
        "date_of_birth": "11/09/1990",
        "company": "Talane",
        "position": "Research Associate",
        "experience": 7,
        "country": "China",
        "phrase": "Multi-channelled coherent leverage",
        "salary": 180025,
}


When dealing with queries that involve categories, groups, or regions (such as language families, geographical areas, or professional fields), expand the search to include all relevant specific instances. 
For example, if asked about Slavic languages, include searches for Russian, Polish, Czech, etc. If asked about people from Europe, include searches for various European countries.


Generate a JSON query for Elasticsearch. Provide only the raw JSON without any surrounding tags or markdown formatting, because we need to convert your response to an object. 
Use a lenient approach with 'should' clauses instead of strict 'must' clauses. Include a 'minimum_should_match' parameter to ensure some relevance while allowing flexibility. Avoid using 'must' clauses entirely.
All queries must be lowercase.

Use 'match' queries instead of 'term' queries to allow for partial matches and spelling variations. Where appropriate, include fuzziness parameters to further increase tolerance for spelling differences. 
For name fields or other phrases where word order matters, consider using 'match_phrase' with a slop parameter. Use 'multi_match' for fields that might contain the value in different subfields.

Now, please convert the following user query into an appropriate Elasticsearch query:

[User's query goes here]
'''


# CLI args for model and base_url
parser = argparse.ArgumentParser(description="Automated faceted search demo")
parser.add_argument(
    "--model",
    default="gpt-3.5-turbo",
    help="LLM model name or gpt-3.5-turbo"
)
parser.add_argument(
    "--base-url",
    default="https://api.openai.com/v1",
    help="LLM API base URL or https://api.openai.com/v1)"
)
config = parser.parse_args()
logging.info("models name: %s base url: %s", config.model, config.base_url)

class OpenAIClient:
    def __init__(self):
        # print(f"OPENAI_API_KEY: {os.environ.get('OPENAI_API_KEY')}")  # just a test to see if the key is set correctly
        self.client = OpenAI(
            api_key = os.environ.get("OPENAI_API_KEY"),
            base_url = config.base_url
        )

    def generate_non_streaming_response(self, prompt, model=config.model, system_prompt=""):
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=4096
        )
        return response.choices[0].message.content
        
LLM = OpenAIClient()

# Elasticsearch Upload Functions

from collections import defaultdict

def bulk_upload_pickle_to_elasticsearch(file_path, index_name, es, batch_size=1000):
    
    total_uploaded = 0
    total_failed = 0
    
    def create_action(doc):
        # doc=merge_nested_dictionaries(doc, default_template)
        
        return {
            "_index": index_name,
            "_id": uuid.uuid4(),
            "_source": doc
        }

    def read_and_upload_batch(data):
        batch = []
        for doc in data:
            batch.append(create_action(doc))
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    with open(file_path, 'rb') as f:
        data=pickle.load(f)
        for batch in read_and_upload_batch(data):
            try:
                success, failed = helpers.bulk(es, batch, raise_on_error=False)
                if type(failed) is list: 
                    failed=len(failed)
                total_uploaded += success
                total_failed += failed
                logging.info("Uploaded %d documents, Failed %d documents", success, failed)
            except Exception as e:
                logging.exception("Error during bulk upload")
                total_failed += len(batch)

    return total_uploaded, total_failed


# Initialize Elasticsearch client

try:
    es_endpoint = os.environ.get("ELASTIC_ENDPOINT")
    es_client = Elasticsearch(
        es_endpoint,
        api_key=os.environ.get("ELASTIC_API_KEY")
        
    )
except Exception as e:
    es_client=None


# clean up the DB
index = os.environ.get("ELASTIC_DATA_INDEX")
logging.info("Cleaning up the DB: %s", index)
if es_client is not None and es_client.indices.exists(index=index):
    es_client.indices.delete(index=index, ignore_unavailable=True)


logging.info("Uploading data to the DB: %s", index)
runs = 1
profile_batch_size=1

for i in range(runs):
    profiles = generate_employee_profiles()
    filename='./data/employees.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(profiles, file)
    try:
        logging.info("Uploading data to the DB: %s", index)
        bulk_upload_pickle_to_elasticsearch(filename, index, es_client)
    except Exception as e:
        logging.exception("Error uploading batch")


# Automated Search
queries = [
    "search for the word “heuristic” in the ”phrase” field in the documents we ingested earlier.",
    "search for the word “heuristic roots help” in the ”phrase” field in the documents",
    "search for the phrase “heuristic roots help” in the documents",
    "search for  any match from “heuristic roots help” in the ”phrase” field in the documents",
]

for query in queries:
    response = LLM.generate_non_streaming_response(query, system_prompt=prompt)
    es_query = json.loads(response)
    logging.info('\nResponse generated from the model: %s to query: %s', config.model, query)
    pprint(es_query)
    try:
        search_results = es_client.search(index=index, body=es_query)
        total_hits = search_results['hits']['total']['value']
        logging.info("Total matches: %s", total_hits)
    except Exception as e:
        logging.exception("Error searching")
