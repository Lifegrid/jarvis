from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from core_llm.llm_client import chat_with_llm
from intent.intent_mapper import detect_intent
from code_executor.code_engine import execute_python_code
from web_scraper.source_vectorizer import store_vector
from web_scraper.web_navigator import fetch_page_content
from web_scraper.content_summarizer import summarize_content
from autonomy.autonomous_executor import run_autonomous_cycle
from suggestion_engine.proactive_suggestions import suggest_actions
from memory_engine.profile_manager import get_user_profile

app = FastAPI()

# Autoriser les requêtes cross-origin (CORS) pour accès frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

class CodeInput(BaseModel):
    code: str

class ScrapeInput(BaseModel):
    url: str

@app.post("/chat")
async def chat_route(data: ChatInput):
    user_message = data.message
    intent = detect_intent(user_message)
    profile = get_user_profile()

    if intent == "generate_and_run_code":
        output, error = execute_python_code(user_message)
        return {"intent": intent, "output": output, "error": error}

    elif intent == "scrape":
        url, html = fetch_page_content(user_message)
        summary = summarize_content(html)
        store_vector(url, summary)
        return {"intent": intent, "summary": summary, "url": url}

    elif intent == "autonomous_cycle":
        result = run_autonomous_cycle(profile)
        return {"intent": intent, "result": result}

    else:
        response = chat_with_llm(user_message)
        return {"intent": intent, "response": response}

@app.get("/suggestions")
async def suggestions():
    profile = get_user_profile()
    return {"suggestions": suggest_actions(profile)}
