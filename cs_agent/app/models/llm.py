from langchain.chat_models import init_chat_model
from app.config.settings import settings


def get_llm():
    return init_chat_model(
        settings.MODEL_NAME,
        temperature=settings.TEMPERATURE
    )