from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Banking Chatbot API",
    description="API for modern banking chatbot powered by LangGraph & Ollama",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Banking Chatbot API is running"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
