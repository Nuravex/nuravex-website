from langchain.messages import HumanMessage


def user_message(text: str) -> HumanMessage:
    return HumanMessage(content=text)
