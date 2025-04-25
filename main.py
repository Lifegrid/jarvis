import os
import json
import re
import uuid
from fastapi import UploadFile
from core.llm_interface import ask_llm
from core.file_processor import summarize_file
from core.web_research import perform_web_research
from core.intent_analyzer import analyze_message
from core.action_executor import execute_action
from core.memory_engine import store_memory_snapshot
from core.self_improvement_engine import generate_and_test_patch

CONVERSATION_DIR = "conversations"
os.makedirs(CONVERSATION_DIR, exist_ok=True)

def sanitize_filename(filename: str) -> str:
    # Supprimer les caractères invalides pour un nom de fichier
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def generate_new_conversation_id():
    """Génère un nouvel ID de conversation unique"""
    return str(uuid.uuid4())

def load_conversation(conversation_id: str) -> list[dict]:
    path = os.path.join(CONVERSATION_DIR, f"{sanitize_filename(conversation_id)}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_message(conversation_id: str, message: dict):
    path = os.path.join(CONVERSATION_DIR, f"{sanitize_filename(conversation_id)}.json")
    history = load_conversation(conversation_id)
    history.append(message)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def generate_reply(conversation_id: str, user_text: str) -> str:
    """
    Analyse le message, détecte une intention, effectue une action si besoin,
    ou fait une recherche web, ou passe au LLM.
    """
    messages = load_conversation(conversation_id)

    # Analyse d’intention
    intent_data = analyze_message(user_text)
    if intent_data["action"]:
        result = execute_action(intent_data["action"])
        save_message(conversation_id, {"from": "user", "text": user_text})
        save_message(conversation_id, {"from": "jarvis", "text": result})
        return result

    # Recherche web si nécessaire
    if should_trigger_web_search(user_text):
        result = perform_web_research(user_text)
        save_message(conversation_id, {"from": "user", "text": user_text})
        save_message(conversation_id, {"from": "jarvis", "text": result})
        return result

    # Dialogue normal avec LLM
    messages.append({"from": "user", "text": user_text})
    context = format_context(messages[-10:])  # mémoire glissante
    reply = ask_llm(context)
    save_message(conversation_id, {"from": "user", "text": user_text})
    save_message(conversation_id, {"from": "jarvis", "text": reply})
    return reply

def format_context(messages: list[dict]) -> list[dict]:
    return [{"role": "user" if m["from"] == "user" else "assistant", "content": m["text"]} for m in messages]

def should_trigger_web_search(text: str) -> bool:
    keywords = ["cours", "dernières nouvelles", "prix", "actualité", "taux", "résultats"]
    return any(k in text.lower() for k in keywords)

def process_uploaded_file(conversation_id: str, file: UploadFile) -> str:
    summary = summarize_file(file)
    save_message(conversation_id, {"from": "user", "text": f"[Fichier] {file.filename}"})
    save_message(conversation_id, {"from": "jarvis", "text": summary})
    store_memory_snapshot(content=summary, category="fichier")
    return summary

def analyze_user_message(message: str) -> dict:
    return analyze_message(message)

def get_bilan() -> str:
    # Bilan quotidien basé sur les souvenirs web et autres sources
    from core.bilan_engine import generate_daily_bilan
    return generate_daily_bilan()
