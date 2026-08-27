# Banking Chatbot

A modern banking chatbot powered by LangGraph, LangChain, FastAPI, Next.js, and Ollama Qwen.

## Architecture

- **Frontend**: Next.js
- **Backend API**: FastAPI
- **Agent Orchestrator**: LangGraph + LangChain
- **LLM Provider**: Ollama (Qwen)
- **Database**: PostgreSQL

## Running Locally

Requirements:
- Node.js
- Python 3.10+
- Docker & Docker Compose (for PostgreSQL)

### Start Infrastructure
```bash
docker-compose up -d
```

### Start Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Start Frontend
```bash
cd frontend
npm install
npm run dev
```
