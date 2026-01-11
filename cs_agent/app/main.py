from langchain.messages import HumanMessage
from app.agent.graph import support_agent
from app.schemas.messages import user_message


def run():
    """
    Application entry point.
    Sends a user message to the customer support agent
    and prints the agent's response.
    """

    # Initial user input
    messages = [user_message("My order is delayed")]

    # Run the agent
    result = support_agent.invoke(
        {"messages": messages}
    )

    # Get the final agent response
    final_message = result["messages"][-1]

    print("\nCustomer Support Response")
    print("-" * 30)
    print(final_message.content)


if __name__ == "__main__":
    run()