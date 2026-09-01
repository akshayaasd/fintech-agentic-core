from fastapi import APIRouter, Depends, status
from app.api.schemas import ChatRequest, ChatResponse, User
from app.api.deps import get_current_active_user
import uuid

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat_endpoint(
    request: ChatRequest,
    current_user: User = Depends(get_current_active_user)
):
    """
    Handle chatbot messages.
    For Phase 3, this returns a structured mock response.
    It will be integrated with the LangGraph orchestrator in Phase 6.
    """
    session_id = request.session_id or str(uuid.uuid4())
    
    # Simple placeholder response
    mock_reply = (
        f"Hello! I am your banking virtual assistant. "
        f"I received your message: '{request.message}'. "
        f"Since the agent orchestrator is still under construction in the backend (Phase 6), "
        f"I'm echoing this response to verify Phase 3 is working properly."
    )
    
    return ChatResponse(
        response=mock_reply,
        session_id=session_id,
        status="success"
    )
