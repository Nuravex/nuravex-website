def test_prompt_not_empty():
    from app.agent.prompts import SUPPORT_SYSTEM_PROMPT
    assert len(SUPPORT_SYSTEM_PROMPT) > 10
