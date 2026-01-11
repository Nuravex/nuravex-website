from langgraph.graph import StateGraph, START, END
from app.agent.state import SupportState
from app.agent.nodes import llm_node
from app.config.constants import LLM_NODE
from app.config.constants import MAX_LLM_CALLS
from typing import Literal

def should_continue(state: SupportState) -> Literal[LLM_NODE, END]:
    if state["llm_calls"] >= MAX_LLM_CALLS:
        return END

    return END

# Create a graph builder with the agent state
builder = StateGraph(SupportState)

# Register nodes
builder.add_node(LLM_NODE, llm_node)

# Define execution flow
builder.add_edge(START, LLM_NODE)
builder.add_conditional_edges(
    LLM_NODE,
    should_continue,
    [LLM_NODE, END]
)

# Compile the graph into a runnable agent
support_agent = builder.compile()
