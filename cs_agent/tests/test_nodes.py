def test_llm_node_exists():
    from app.agent.nodes import llm_node
    assert callable(llm_node)
