from langchain.chat_models import init_chat_model


def get_llm():
    return init_chat_model(
        "claude-sonnet-4-5-20250929",
        temperature=0.3
    )