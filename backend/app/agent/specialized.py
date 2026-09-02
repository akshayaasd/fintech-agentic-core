from langchain_core.messages import AIMessage
from langgraph.prebuilt import create_react_agent
from app.agent.state import AgentState
from app.llm.factory import get_llm_provider
from app.agent.tools import (
    get_account_balance, get_account_details,
    transfer_funds, get_recent_transactions,
    request_cheque_book, update_kyc
)

# Initialize the LLM for the specialized sub-graphs
llm = get_llm_provider().get_model()

# -------------------------------------------------------------------------
# Accounts Sub-Graph
# -------------------------------------------------------------------------
accounts_tools = [get_account_balance, get_account_details]
accounts_system_prompt = "You are the Accounts Agent. Help the user with their account inquiries."
accounts_graph = create_react_agent(llm, tools=accounts_tools, state_modifier=accounts_system_prompt)

async def accounts_agent_node(state: AgentState):
    """Accounts Agent Node executing its tool-calling sub-graph"""
    result = await accounts_graph.ainvoke({"messages": state["messages"]})
    return {"messages": result["messages"]}

# -------------------------------------------------------------------------
# Transactions Sub-Graph
# -------------------------------------------------------------------------
transactions_tools = [transfer_funds, get_recent_transactions]
transactions_system_prompt = "You are the Transactions Agent. Help the user with fund transfers and recent transactions."
transactions_graph = create_react_agent(llm, tools=transactions_tools, state_modifier=transactions_system_prompt)

async def transactions_agent_node(state: AgentState):
    """Transactions Agent Node executing its tool-calling sub-graph"""
    result = await transactions_graph.ainvoke({"messages": state["messages"]})
    return {"messages": result["messages"]}

# -------------------------------------------------------------------------
# Service Sub-Graph
# -------------------------------------------------------------------------
service_tools = [request_cheque_book, update_kyc]
service_system_prompt = "You are the Service Agent. Help the user with KYC updates and cheque book requests."
service_graph = create_react_agent(llm, tools=service_tools, state_modifier=service_system_prompt)

async def service_agent_node(state: AgentState):
    """Service Agent Node executing its tool-calling sub-graph"""
    result = await service_graph.ainvoke({"messages": state["messages"]})
    return {"messages": result["messages"]}
