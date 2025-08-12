#!/usr/bin/env python3
"""
OpenAI API Key Test Utility

This script tests your OpenAI API key by making a simple API call.
It reads the key from the .env file and validates it works.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
import sys

def test_openai_connection():
    """Test the OpenAI API connection and key validity."""
    
    print("🔍 Testing OpenAI API Connection...")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found in environment variables")
        print("   Make sure you have a .env file with OPENAI_API_KEY=your_key_here")
        return False
    
    # Check if key format looks correct
    if not api_key.startswith(('sk-', 'sk-proj-')):
        print("❌ ERROR: API key format appears incorrect")
        print(f"   Expected format: sk-... or sk-proj-...")
        print(f"   Your key starts with: {api_key[:10]}...")
        return False
    
    print(f"✅ API key found: {api_key[:10]}...{api_key[-4:]}")
    
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        print("✅ OpenAI client initialized successfully")
        
        # Test with a simple completion
        print("🧪 Making test API call...")
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using cheaper model for testing
            messages=[
                {"role": "user", "content": "Say 'Hello, API test successful!' and nothing else."}
            ],
            max_tokens=50
        )
        
        response_text = response.choices[0].message.content.strip()
        print(f"✅ API Response: {response_text}")
        
        # Check usage information
        if hasattr(response, 'usage'):
            print(f"📊 Tokens used: {response.usage.total_tokens}")
        
        print("\n🎉 SUCCESS: OpenAI API is working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ ERROR: API call failed")
        print(f"   Error type: {type(e).__name__}")
        print(f"   Error message: {str(e)}")
        
        # Provide helpful error messages
        if "authentication" in str(e).lower() or "unauthorized" in str(e).lower():
            print("\n💡 Troubleshooting:")
            print("   - Check that your API key is correct")
            print("   - Make sure you have credits in your OpenAI account")
            print("   - Verify the key hasn't expired")
        
        return False

def test_models():
    """Test listing available models."""
    try:
        load_dotenv()
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
        print("\n🔍 Testing model access...")
        models = client.models.list()
        
        # Show some available models
        gpt_models = [model.id for model in models.data if 'gpt' in model.id.lower()][:5]
        print(f"✅ Available GPT models (showing first 5): {gpt_models}")
        
    except Exception as e:
        print(f"⚠️  Could not list models: {e}")

def main():
    """Main function to run all tests."""
    print("OpenAI API Test Utility")
    print("=====================\n")
    
    # Test basic connection
    success = test_openai_connection()
    
    if success:
        # Test model listing
        test_models()
        
        print("\n✨ All tests passed! Your OpenAI setup is ready to use.")
        sys.exit(0)
    else:
        print("\n❌ Tests failed. Please fix the issues above before proceeding.")
        sys.exit(1)

if __name__ == "__main__":
    main() 