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

import pickle
import argparse
load_dotenv()

from generate_synthetic_data import generate_profiles


print_search_results = False

prompt='''
You are an AI assistant specialized in converting natural language queries into Elasticsearch queries. 
Your task is to interpret user questions about personal profiles and generate the appropriate Elasticsearch query in JSON format.

The document schema for the profiles is as follows:

{
  "nric": "string",
  "name": "string",
  "race": "string",
  "gender": "string",
  "date_of_birth": "date",
  "age": "integer",
  "country_of_birth": "string",
  "citizenship": "string",
  "religion": "string" ["Buddhism", "Christianity", "Islam", "Hinduism", "Taoism", "No Religion"],
  "marital_status": "string" ["Single", "Married", "Divorced", "Separated", "Widowed", "Civil Partnership", "Domestic Partnership", "Engaged", "Annulled"],
  "address": {
    "block": "string",
    "street_no": "string",
    "street": "string",
    "unit": "string",
    "town": "string",
    "postal_code": "string"
  },
  "phone_number": "string",
  "email": "string",
  "occupation": "string",
  "cpf_number": "string",
  "education": {
    "highest_qualification": "string",
    "institution": "string"
  },
  "languages": {
    "spoken": {"language":"fluency" ["Basic", "Conversational", "Fluent", "Native"]},
    "written": {"language":"fluency" ["Basic", "Conversational", "Fluent", "Native"]},
  },
  "height_cm": "integer",
  "weight_kg": "integer",
  "blood_type": "string" ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"],
  "passport_number": "string",
  "drivers_license_number": "string",
  "national_service": {
    "status": "string",
    "rank": "string"
  },
  "immigration_status": "string",
  "emergency_contact": {
    "name": "string",
    "relationship": "string",
    "phone_number": "string"
  },
  "deceased": "boolean",
  "date_of_death": "date"
}

Example query:
User: Find all male Singapore citizens between 25 and 30 years old who work as software developers and speak fluent English.

Your response should be:

{
  "query": {
    "bool": {
      "should": [
        { "match": { "gender": "Male" } },
        { "match": { "citizenship": "Singapore Citizen" } },
        { "range": { "age": { "gte": 25, "lte": 30 } } },
        { "match": { "occupation": "Software Developer" } },
        {
          "match": {
            "languages.spoken.English": {
              "query": "Fluent",
              "fuzziness": "AUTO"
            }
          }
        }
      ],
      "minimum_should_match": 2
    }
  }
}

Consider using multi_match for fields that might contain the value in different subfields:
{
  "multi_match": {
    "query": "Software Developer",
    "fields": ["occupation", "job_title", "role"],
    "type": "best_fields",
    "fuzziness": "AUTO"
  }
}

For names or other fields where word order matters, you might want to use match_phrase with slop:
{
  "match_phrase": {
    "full_name": {
      "query": "John Doe",
      "slop": 1
    }
  }
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
print(f"models name: {config.model} \n base url: {config.base_url} \n")


class OpenAIClient:
    def __init__(self):
        # print(f"OPENAI_API_KEY: {os.environ.get('OPENAI_API_KEY')}")  # just a test to see if the key is set correctly
        self.client = OpenAI(
            api_key = os.environ.get("OPENAI_API_KEY"),
            base_url = config.base_url
        )

    def generate_streaming_response(self, prompt, model=config.model, system_prompt=""):
        """Generate streaming response (simplified for script version)"""
        response_text = ""
        for chunk in self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            stream=True,
            max_tokens=4096
        ):
            if len(chunk.choices) > 0:
                if chunk.choices[0].delta.content is not None:
                    response_text += chunk.choices[0].delta.content
                    print(chunk.choices[0].delta.content, end="", flush=True)
        print()  # New line after streaming
        return response_text

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
                print(f"Uploaded {success} documents, Failed {failed} documents")
            except Exception as e:
                print(f"Error during bulk upload: {str(e)}")
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
print(f'Cleaning up the DB: {os.environ["ELASTIC_DATA_INDEX"]}')
index = os.environ["ELASTIC_DATA_INDEX"]
if es_client.indices.exists(index=index):
    es_client.indices.delete(index=index, ignore_unavailable=True)


# Storage loads 402.77MB,  Document count 200,000, take 4.5 minutes to load.
print(f'Uploading data to the DB: {os.environ["ELASTIC_DATA_INDEX"]}')
# runs=200
runs = 10
profile_batch_size=1000

for i in range(runs):
    profiles = generate_profiles(profile_batch_size)
    filename='./data/personal_info.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(profiles, file)
    try:
        bulk_upload_pickle_to_elasticsearch(filename, os.environ.get("ELASTIC_DATA_INDEX"), es_client)
    except Exception as e:
        print(traceback.print_exc())


# Automated Search
# Test 1

query="All non-Singaporean men over the age of 25 who are software people living in woodlands" 
response=LLM.generate_non_streaming_response(query, system_prompt=prompt)
es_query=json.loads(response)
print(f'\nResponse generated from the model: {config.model} \nto query: {query}')
pprint(es_query)


try:
  search_results = es_client.search(index=os.environ.get("ELASTIC_DATA_INDEX"), body=es_query)  


  total_hits = search_results['hits']['total']['value']
  print(f"Total matches: {total_hits}")

  if print_search_results:
      for hit in search_results['hits']['hits']:
          print(f"Score: {hit['_score']}")
          print(f"Name: {hit['_source']['name']}")
          print(f"Age: {hit['_source']['age']}")
          print(f"Gender: {hit['_source']['gender']}")
          print(f"Citizenship: {hit['_source']['citizenship']}")
          print(f"Occupation: {hit['_source']['occupation']}")
          print(f"Address: {hit['_source']['address']}")
          print("---")
except Exception as e:
    print(traceback.print_exc())
    print(f'Error: {e}')

# Test 2

query="Women who are not alive currently, who are universal blood donors born in singapore" 
response=LLM.generate_non_streaming_response(query, system_prompt=prompt)
es_query=json.loads(response)
print(f'\nResponse generated from the model: {config.model} \nto query: {query}')
pprint(es_query)

try:
  search_results = es_client.search(index=os.environ.get("ELASTIC_DATA_INDEX"), body=es_query)


  total_hits = search_results['hits']['total']['value']
  print(f"Total matches: {total_hits}")

  if print_search_results:
      for hit in search_results['hits']['hits']:
          print(f"Score: {hit['_score']}")
          print(f"Name: {hit['_source']['name']}")
          print(f"Blood Type: {hit['_source']['blood_type']}")
          print(f"Gender: {hit['_source']['gender']}")
          print(f"Country of Birth: {hit['_source']['country_of_birth']}")
          print(f"Deceased: {hit['_source']['deceased']}")
          print("---")
except Exception as e:
    print(traceback.print_exc())
    print(f'Error: {e}')

# Test 3

# query="People who speak chinese dialects" 
query="People who speak chinese dialects fluently" 
response=LLM.generate_non_streaming_response(query, system_prompt=prompt)
es_query=json.loads(response)
print(f'\nResponse generated from the model: {config.model} \nto query: {query}')
pprint(es_query)

try:
  search_results = es_client.search(index=os.environ.get("ELASTIC_DATA_INDEX"), body=es_query)


  total_hits = search_results['hits']['total']['value']
  print(f"Total matches: {total_hits}")

  if print_search_results:
      for hit in search_results['hits']['hits']:
          print(f"Score: {hit['_score']}")
          print(f"Name: {hit['_source']['name']}")
          print(f"languages: {hit['_source']['languages']}")
          print("---")
except Exception as e:
    print(traceback.print_exc())
    print(f'Error: {e}')
