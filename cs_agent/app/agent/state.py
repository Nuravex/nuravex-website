from typing_extensions import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

class SupportState(TypedDict):
    """
    Shared state for the customer support agent.
    """
    messages:Annotated[list[AnyMessage],operator.add]
    llm_calls:int