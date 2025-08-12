#!/usr/bin/env python3
"""
Debug Elasticsearch Connection
"""

import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

# Load environment variables
load_dotenv()

print("🔍 Debugging Elasticsearch Configuration")
print("=" * 40)

# Check environment variables
es_endpoint = os.environ.get("ELASTIC_ENDPOINT")
es_api_key = os.environ.get("ELASTIC_API_KEY")
es_index = os.environ.get("ELASTIC_DATA_INDEX")

print(f"ELASTIC_ENDPOINT: {es_endpoint}")
print(f"ELASTIC_API_KEY: {'✅ Set' if es_api_key else '❌ Empty'}")
print(f"ELASTIC_DATA_INDEX: {es_index}")

# Test the exact same connection code from the notebook
print("\n🧪 Testing connection code from notebook...")
try:
    es_client = Elasticsearch(
        es_endpoint,
        api_key=es_api_key
    )
    print("✅ Connection successful!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("   This is why es_client is None in the notebook") 