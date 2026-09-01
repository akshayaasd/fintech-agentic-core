from app.core.config import settings
from app.llm.provider import BaseLLMProvider, OllamaProvider
import logging

logger = logging.getLogger(__name__)

def get_llm_provider() -> BaseLLMProvider:
    """
    Factory function to initialize and return the selected LLM provider based on settings.
    """
    provider = settings.LLM_PROVIDER.lower()
    
    if provider == "ollama":
        logger.info(f"Initializing Ollama Provider with model: {settings.OLLAMA_MODEL}")
        return OllamaProvider(
            base_url=settings.OLLAMA_BASE_URL,
            model=settings.OLLAMA_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            timeout=settings.LLM_TIMEOUT_SECONDS
        )
    else:
        raise ValueError(f"Unsupported LLM provider configured: {provider}")
