import asyncio
import os
import sys

# Add app to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.llm.factory import get_llm_provider

async def main():
    print("Testing LLM Factory initialization...")
    try:
        provider = get_llm_provider()
        print(f"Provider initialized successfully: {provider}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
