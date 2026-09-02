from fastapi import APIRouter, Depends, status
from app.api.schemas import ChatRequest, ChatResponse, User
from app.api.deps import get_current_active_user
from app.agent.graph import graph_app
from langchain_core.messages import HumanMessage
import uuid

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat_endpoint(
    request: ChatRequest,
    current_user: User = Depends(get_current_active_user)
):
    """
    Handle chatbot messages.
    For Phase 6, this integrates the LangGraph orchestrator.
    """
    session_id = request.session_id or str(uuid.uuid4())
    agent_used = "coordinator"
    
    try:
        # In Phase 10 (Session Store), we will fetch history based on session_id
        # For now, we just send the current message as a HumanMessage
        inputs = {"messages": [HumanMessage(content=request.message)]}
        
        # Invoke the LangGraph application
        result = await graph_app.ainvoke(inputs)
        
        # Extract the final message
        final_message = result["messages"][-1].content
        agent_used = result.get("next_agent", "general")
        reply_content = final_message
    except Exception as e:
        reply_content = f"I'm sorry, I encountered an error in the orchestrator: {str(e)}"
        agent_used = "error"
    
    return ChatResponse(
        session_id=session_id,
        reply=reply_content,
        agent_used=agent_used,
        actions_taken=[],
        cost=0.0
    )
