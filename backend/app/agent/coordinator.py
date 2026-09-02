import json
from langchain_core.messages import SystemMessage, HumanMessage
from app.llm.factory import get_llm_provider
from app.agent.state import AgentState

# The coordinator intent detection prompt
COORDINATOR_PROMPT = """You are the Coordinator Agent for a banking virtual assistant.
Your job is to analyze the user's latest message and route it to the appropriate specialized agent.

Agents available:
1. "accounts": For inquiries related to account balance, account details, statements.
2. "transactions": For fund transfers, sending money, transaction history, payments.
3. "service": For profile updates, KYC, address changes, cheque book requests.
4. "general": For greetings, small talk, or any query that does not fit the above categories.

Respond ONLY with a JSON object containing a single key "next_agent" mapping to one of the four agents above.
Example: {"next_agent": "accounts"}
"""

async def coordinator_node(state: AgentState):
    """
    Analyzes the latest user message and determines the next agent to route to.
    """
    messages = state["messages"]
    if not messages:
        # Default fallback if no messages
        return {"next_agent": "general"}

    user_msg = messages[-1]
    
    # We use a distinct LLM call for intent detection, ensuring JSON output
    llm = get_llm_provider().get_model()
    
    # Instruct the model to return JSON
    # We bind format="json" which works nicely with Ollama
    llm_with_json = llm.bind(format="json")
    
    system_message = SystemMessage(content=COORDINATOR_PROMPT)
    # We only send the last message for routing to keep it focused
    routing_messages = [system_message, HumanMessage(content=user_msg.content)]
    
    try:
        response = await llm_with_json.ainvoke(routing_messages)
        content = response.content
        data = json.loads(content)
        next_agent = data.get("next_agent", "general")
        
        # Validate next_agent
        if next_agent not in ["accounts", "transactions", "service", "general"]:
            next_agent = "general"
            
    except Exception as e:
        # Fallback to general if JSON parsing or LLM fails
        print(f"Coordinator error: {e}")
        next_agent = "general"
        
    return {"next_agent": next_agent}

async def general_agent_node(state: AgentState):
    """
    Handles general small talk and fallback responses.
    """
    llm = get_llm_provider()
    
    system_prompt = SystemMessage(content=(
        "You are a helpful banking assistant. The user has asked a general question "
        "or made small talk. Be polite, concise, and helpful."
    ))
    
    # Prepend system prompt to the conversation history
    messages_to_send = [system_prompt] + list(state["messages"])
    
    response = await llm.agenerate_response(messages_to_send)
    return {"messages": [response]}
