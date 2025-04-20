from app.services.ollama_client import OllamaClient

class ConstructionAssistantAgent:
    def __init__(self):
        self.llm = OllamaClient()

    def respond(self, question: str) -> str:
        return self.llm.ask(question)

