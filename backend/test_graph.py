import asyncio
import os
import sys
from langchain_core.messages import HumanMessage

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.agent.graph import graph_app

async def main():
    print("Testing LangGraph Agent Orchestrator...")
    
    test_messages = [
        "What is my account balance?",
        "I need a new cheque book.",
        "Transfer $50 to Alice.",
        "Hello, how are you today?"
    ]
    
    for msg in test_messages:
        print(f"\n--- User: {msg} ---")
        try:
            inputs = {"messages": [HumanMessage(content=msg)]}
            result = await graph_app.ainvoke(inputs)
            
            final_message = result["messages"][-1].content
            next_agent = result.get("next_agent", "unknown")
            
            print(f"Routed to Agent: {next_agent}")
            print(f"Response: {final_message}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
