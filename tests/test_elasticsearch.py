#!/usr/bin/env python3
"""
Elasticsearch Connection Test Utility

This script tests your Elasticsearch connection and helps diagnose common issues.
"""

import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
import sys

def test_elasticsearch_connection():
    """Test the Elasticsearch connection and configuration."""
    
    print("🔍 Testing Elasticsearch Connection...")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Get configuration
    es_endpoint = os.environ.get("ELASTIC_ENDPOINT")
    es_api_key = os.environ.get("ELASTIC_API_KEY")
    es_index = os.environ.get("ELASTIC_DATA_INDEX")
    
    print(f"📋 Configuration Check:")
    print(f"   Endpoint: {es_endpoint}")
    print(f"   API Key: {'✅ Set' if es_api_key else '❌ Missing'}")
    print(f"   Index: {es_index}")
    
    # Check if required variables are set
    if not es_endpoint:
        print("\n❌ ERROR: ELASTIC_ENDPOINT not found")
        print("   Add ELASTIC_ENDPOINT=your_endpoint to your .env file")
        return False
    
    if not es_api_key:
        print("\n❌ ERROR: ELASTIC_API_KEY not found")
        print("   Add ELASTIC_API_KEY=your_api_key to your .env file")
        return False
    
    if not es_index:
        print("\n❌ ERROR: ELASTIC_DATA_INDEX not found")
        print("   Add ELASTIC_DATA_INDEX=your_index_name to your .env file")
        return False
    
    print("\n✅ All environment variables are set")
    
    try:
        # Test connection
        print("\n🧪 Testing connection...")
        
        # Create client with error handling
        es_client = Elasticsearch(
            es_endpoint,
            api_key=es_api_key,
            verify_certs=True,  # Set to False if using self-signed certs
            ssl_show_warn=False
        )
        
        # Test if client is properly initialized
        if es_client is None:
            print("❌ ERROR: Elasticsearch client is None")
            return False
        
        print("✅ Elasticsearch client created successfully")
        
        # Test connection with ping
        print("🏓 Pinging Elasticsearch...")
        if es_client.ping():
            print("✅ Connection successful!")
        else:
            print("❌ Connection failed - ping unsuccessful")
            return False
        
        # Get cluster info
        print("\n📊 Cluster Information:")
        info = es_client.info()
        print(f"   Cluster Name: {info.get('cluster_name', 'Unknown')}")
        print(f"   Version: {info.get('version', {}).get('number', 'Unknown')}")
        
        # Check if index exists
        print(f"\n🔍 Checking index '{es_index}'...")
        if es_client.indices.exists(index=es_index):
            print(f"✅ Index '{es_index}' exists")
            
            # Get index stats
            stats = es_client.indices.stats(index=es_index)
            doc_count = stats['indices'][es_index]['total']['docs']['count']
            print(f"   Document count: {doc_count}")
        else:
            print(f"⚠️  Index '{es_index}' does not exist")
            print("   This is normal if you haven't uploaded data yet")
        
        print("\n🎉 SUCCESS: Elasticsearch is working correctly!")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: Connection failed")
        print(f"   Error type: {type(e).__name__}")
        print(f"   Error message: {str(e)}")
        
        # Provide helpful troubleshooting tips
        print("\n💡 Troubleshooting:")
        
        if "certificate" in str(e).lower() or "ssl" in str(e).lower():
            print("   - SSL certificate issue. Try setting verify_certs=False")
            print("   - Check if your endpoint uses HTTPS")
        
        if "authentication" in str(e).lower() or "unauthorized" in str(e).lower():
            print("   - Check your API key is correct")
            print("   - Verify the API key has proper permissions")
        
        if "connection" in str(e).lower() or "timeout" in str(e).lower():
            print("   - Check your endpoint URL is correct")
            print("   - Verify network connectivity")
            print("   - Check if Elasticsearch is running")
        
        if "not found" in str(e).lower():
            print("   - Check your endpoint URL")
            print("   - Verify the cluster exists and is accessible")
        
        return False

def test_basic_operations():
    """Test basic Elasticsearch operations."""
    try:
        load_dotenv()
        es_client = Elasticsearch(
            os.environ.get("ELASTIC_ENDPOINT"),
            api_key=os.environ.get("ELASTIC_API_KEY")
        )
        
        # Test a simple search
        print("\n🧪 Testing basic search operation...")
        result = es_client.search(index=os.environ.get("ELASTIC_DATA_INDEX"), body={"query": {"match_all": {}}, "size": 1})
        print(f"✅ Search operation successful")
        print(f"   Total hits: {result['hits']['total']['value']}")
        
    except Exception as e:
        print(f"⚠️  Basic operations test failed: {e}")

def main():
    """Main function to run all tests."""
    print("Elasticsearch Connection Test Utility")
    print("===================================\n")
    
    # Test basic connection
    success = test_elasticsearch_connection()
    
    if success:
        # Test basic operations
        test_basic_operations()
        
        print("\n✨ All tests passed! Your Elasticsearch setup is ready to use.")
        sys.exit(0)
    else:
        print("\n❌ Tests failed. Please fix the issues above before proceeding.")
        sys.exit(1)

if __name__ == "__main__":
    main() 