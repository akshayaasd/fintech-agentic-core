from langchain_core.messages import AIMessage
from app.agent.state import AgentState

async def accounts_agent_node(state: AgentState):
    """Stub for Accounts Agent (Phase 7)"""
    return {"messages": [AIMessage(content="[Accounts Agent Stub] I can help with your account details. (Full implementation in Phase 7)")]}

async def transactions_agent_node(state: AgentState):
    """Stub for Transactions Agent (Phase 7)"""
    return {"messages": [AIMessage(content="[Transactions Agent Stub] I can help you with transfers and payments. (Full implementation in Phase 7)")]}

async def service_agent_node(state: AgentState):
    """Stub for Service Agent (Phase 7)"""
    return {"messages": [AIMessage(content="[Service Agent Stub] I can help you with cheque books and KYC updates. (Full implementation in Phase 7)")]}
