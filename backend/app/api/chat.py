from fastapi import APIRouter, Depends, status
from app.api.schemas import ChatRequest, ChatResponse, User
from app.api.deps import get_current_active_user
from app.llm.factory import get_llm_provider
from app.llm.prompts import get_chat_prompt_template
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
    For Phase 5, this returns a real LLM response from the configured provider (e.g., Ollama).
    It will be integrated with the LangGraph orchestrator in Phase 6.
    """
    session_id = request.session_id or str(uuid.uuid4())
    
    try:
        llm_provider = get_llm_provider()
        prompt_template = get_chat_prompt_template()
        
        # We only pass the current message for now.
        # In Phase 10 (Session Store), we will fetch history based on session_id
        messages = prompt_template.format_messages(messages=[HumanMessage(content=request.message)])
        
        response = await llm_provider.agenerate_response(messages)
        reply_content = response.content
    except Exception as e:
        reply_content = f"I'm sorry, I encountered an error connecting to the LLM: {str(e)}"
    
    return ChatResponse(
        session_id=session_id,
        reply=reply_content,
        agent_used="llm_agent",
        actions_taken=[],
        cost=0.0
    )
