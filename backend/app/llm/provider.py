from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import httpx
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage
from langchain_ollama import ChatOllama
import logging

logger = logging.getLogger(__name__)

class BaseLLMProvider(ABC):
    @abstractmethod
    def get_model(self) -> BaseChatModel:
        pass
    
    @abstractmethod
    async def agenerate_response(self, messages: List[BaseMessage]) -> BaseMessage:
        pass

class OllamaProvider(BaseLLMProvider):
    def __init__(self, base_url: str, model: str, temperature: float = 0.0, timeout: int = 30):
        self.base_url = base_url
        self.model = model
        self.temperature = temperature
        
        # We configure httpx Client for explicit timeouts
        timeout_config = httpx.Timeout(timeout)
        self.client = httpx.AsyncClient(timeout=timeout_config)
        
        self.chat_model = ChatOllama(
            base_url=self.base_url,
            model=self.model,
            temperature=self.temperature,
            client=self.client
        )
    
    def get_model(self) -> BaseChatModel:
        return self.chat_model

    async def agenerate_response(self, messages: List[BaseMessage]) -> BaseMessage:
        """
        Generates a response from Ollama asynchronously with basic error handling.
        """
        try:
            response = await self.chat_model.ainvoke(messages)
            return response
        except Exception as e:
            logger.error(f"Error calling Ollama model: {str(e)}")
            raise e
