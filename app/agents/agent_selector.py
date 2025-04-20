from app.agents.agent_registry import AGENT_PROFILES

def select_agent(agent_key: str) -> str:
    return AGENT_PROFILES.get(agent_key.lower(), AGENT_PROFILES["assistant"])
