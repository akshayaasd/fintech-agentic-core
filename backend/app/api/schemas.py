from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID

class ChatMessage(BaseModel):
    role: str = Field(..., description="Role of the message sender (e.g. 'user', 'assistant')")
    content: str = Field(..., description="Text content of the message")

class ChatRequest(BaseModel):
    message: str = Field(..., description="The user's query or message to the chatbot")
    session_id: Optional[str] = Field(None, description="Unique identifier for the chat session. If not provided, a new one may be created.")

class ChatResponse(BaseModel):
    response: str = Field(..., description="The assistant's generated response")
    session_id: str = Field(..., description="The session identifier associated with the request/response")
    status: str = Field("success", description="Status of the request execution ('success', 'error')")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

