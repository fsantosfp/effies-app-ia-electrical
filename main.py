from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.agent_selector import select_agent
from app.services.ollama_client import chat_with_ollama


app = FastAPI()

class UserInput(BaseModel):
    message: str
    agent: str

@app.post("/ask")
async def ask_agent (input: UserInput):

    agent = select_agent(input.agent)
    full_prompt = f"{agent['prompt']}\n\nUser: {input.message}"

    print(f"🔧 DEBUG — Usando agente: {agent['name']}")

    try:

        response = chat_with_ollama(full_prompt)
        
        return {
            "agent": agent['name'],
            "response": response
        }
    
    except Exception as e:
        return {"error": str(e), "details": type(e).__name__}

    

    # response = agent.respond(input.message)
    # return MessageResponse(response=response)