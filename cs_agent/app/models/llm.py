from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama
from app.config.settings import settings


def get_llm():
    return ChatOllama(
        model=settings.MODEL_NAME,
        temperature=settings.TEMPERATURE,
        base_url="http://localhost:11434"
    )