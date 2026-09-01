from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

SYSTEM_PROMPT = """You are a helpful, secure, and professional virtual banking assistant.
Your goal is to assist the user with banking inquiries.
Do not hallucinate any personal information.
If you do not know the answer, politely state so.
Keep your answers concise and clear."""

def get_chat_prompt_template() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="messages"),
    ])
