from langchain.messages import SystemMessage
from app.models.llm import get_llm
from app.agent.prompts import SUPPORT_SYSTEM_PROMPT
from app.agent.state import SupportState


# Initialize the LLM once
llm = get_llm()


def llm_node(state: SupportState):
    """
    LLM node:
    - Reads conversation from state
    - Calls the language model
    - Appends the response back to state
    """

    response = llm.invoke(
        [
            SystemMessage(content=SUPPORT_SYSTEM_PROMPT)
        ] + state["messages"]
    )

    return {
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1
    }