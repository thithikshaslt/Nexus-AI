from django.db import transaction
from abc import ABC, abstractmethod
from chatapp.models import ModelProvider, GlobalResponseCounter

class LLMStub(ABC):
    """Abstract class for stubbed LLM providers."""
    
    @abstractmethod
    def generate_response(self, model: str, prompt: str) -> dict:
        pass

    @staticmethod
    def get_next_response_id() -> str:
        """Fetch and increment the global response counter atomically."""
        with transaction.atomic():
            counter, created = GlobalResponseCounter.objects.get_or_create(id=1)
            counter.count += 1
            counter.save()
        return f"response_{counter.count:03d}" 

class OpenAIStub(LLMStub):
    """Stub response for OpenAI provider."""
    def generate_response(self, model: str, prompt: str) -> dict:
        response_id = self.get_next_response_id()
        return {
            "provider": "openai",
            "model": model,
            "response": "OpenAI: Processed your prompt with advanced language understanding.",
            "response_id": response_id
        }

class AnthropicStub(LLMStub):
    """Stub response for Anthropic provider."""
    def generate_response(self, model: str, prompt: str) -> dict:
        response_id = self.get_next_response_id()
        return {
            "provider": "anthropic",
            "model": model,
            "response": "Anthropic: Your prompt has been interpreted with ethical AI principles.",
            "response_id": response_id
        }
class GeminiStub(LLMStub):
    """Stub response for Gemini provider."""
    def generate_response(self, model: str, prompt: str) -> dict:
        response_id = self.get_next_response_id()
        return {
            "provider": "gemini",
            "model": model,
            "response": "Gemini: Processed your prompt with cutting-edge AI capabilities.",
            "response_id": response_id
        }

class LLMStubManager:
    """Manages routing of LLM requests to the appropriate provider."""
    PROVIDERS = {
        "openai": OpenAIStub(),
        "anthropic": AnthropicStub(),
        "gemini": GeminiStub(),
    }

    #TODO : find a way to deal with new providers if needed


    @classmethod
    def get_response(cls, provider_name: str, model_name: str, prompt: str) -> dict:
        """Routes request to the correct provider stub."""
        if provider_name not in cls.PROVIDERS:
            return {"error": "Invalid provider, must alter LLMStubManager.PROVIDERS"}

        if not ModelProvider.objects.filter(provider_name=provider_name, model_name=model_name).exists():
            return {"error": "Model not supported under this provider"}

        return cls.PROVIDERS[provider_name].generate_response(model_name, prompt)
