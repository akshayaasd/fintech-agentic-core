from langgraph.graph import StateGraph, END
from app.agent.state import AgentState
from app.agent.coordinator import coordinator_node, general_agent_node
from app.agent.specialized import accounts_agent_node, transactions_agent_node, service_agent_node

def route_request(state: AgentState) -> str:
    """
    Conditional routing function based on the coordinator's decision.
    """
    next_agent = state.get("next_agent", "general")
    return next_agent

def build_graph():
    """
    Constructs the LangGraph application.
    """
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("coordinator", coordinator_node)
    workflow.add_node("general", general_agent_node)
    workflow.add_node("accounts", accounts_agent_node)
    workflow.add_node("transactions", transactions_agent_node)
    workflow.add_node("service", service_agent_node)
    
    # Add edges
    workflow.set_entry_point("coordinator")
    
    workflow.add_conditional_edges(
        "coordinator",
        route_request,
        {
            "accounts": "accounts",
            "transactions": "transactions",
            "service": "service",
            "general": "general"
        }
    )
    
    # Add edges from agents to END
    workflow.add_edge("accounts", END)
    workflow.add_edge("transactions", END)
    workflow.add_edge("service", END)
    workflow.add_edge("general", END)
    
    # Compile the graph
    app = workflow.compile()
    
    return app

# Singleton compiled graph instance
graph_app = build_graph()
