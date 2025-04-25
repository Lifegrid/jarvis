from fastapi import FastAPI, UploadFile, HTTPException
import os
from core.llm_interface import ask_llm
from core.file_processor import summarize_file
from core.web_research import perform_web_research
from core.web_memory import search_web_memory
from core.intent_analyzer import analyze_message
from core.action_executor import execute_action
from core.memory_engine import store_memory_snapshot
from core.self_improvement_engine import generate_and_test_patch
from core.super_powers_discovery import discover_new_superpowers
from core.bilan_engine import generate_daily_bilan

# Initialisation de l'instance FastAPI
app = FastAPI()

# Définir les constantes
CONVERSATION_DIR = "conversations"
os.makedirs(CONVERSATION_DIR, exist_ok=True)

# Fonction pour charger une conversation
def load_conversation(conversation_id: str) -> list[dict]:
    path = os.path.join(CONVERSATION_DIR, f"{conversation_id}.json")
    if os.path.exists(path):
        import json
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Fonction pour sauvegarder un message dans une conversation
def save_message(conversation_id: str, message: dict):
    path = os.path.join(CONVERSATION_DIR, f"{conversation_id}.json")
    history = load_conversation(conversation_id)
    history.append(message)
    with open(path, "w", encoding="utf-8") as f:
        import json
        json.dump(history, f, ensure_ascii=False, indent=2)

# Fonction pour générer une réponse à partir du message de l'utilisateur
def generate_reply(conversation_id: str, user_text: str) -> str:
    """
    Analyse le message de l'utilisateur, détecte une intention, effectue une action si nécessaire,
    effectue une recherche web ou fait appel au LLM pour une réponse plus générale.
    """
    messages = load_conversation(conversation_id)

    # Analyse d'intention
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
    context = format_context(messages[-10:])  # Utilisation de la mémoire glissante
    reply = ask_llm(context)
    save_message(conversation_id, {"from": "user", "text": user_text})
    save_message(conversation_id, {"from": "jarvis", "text": reply})
    return reply

# Fonction pour formater les messages en contexte LLM
def format_context(messages: list[dict]) -> list[dict]:
    return [{"role": "user" if m["from"] == "user" else "assistant", "content": m["text"]} for m in messages]

# Fonction pour déterminer si une recherche web est nécessaire
def should_trigger_web_search(text: str) -> bool:
    keywords = ["cours", "dernières nouvelles", "prix", "actualité", "taux", "résultats"]
    return any(k in text.lower() for k in keywords)

# Fonction pour traiter un fichier téléchargé et générer un résumé
def process_uploaded_file(conversation_id: str, file: UploadFile) -> str:
    summary = summarize_file(file)
    save_message(conversation_id, {"from": "user", "text": f"[Fichier] {file.filename}"})
    save_message(conversation_id, {"from": "jarvis", "text": summary})
    store_memory_snapshot(content=summary, category="fichier")
    return summary

# Fonction pour analyser un message de l'utilisateur
def analyze_user_message(message: str) -> dict:
    return analyze_message(message)

# Fonction pour générer un bilan quotidien basé sur les souvenirs
def get_bilan() -> str:
    return generate_daily_bilan()

# Endpoint pour découvrir des super-pouvoirs
@app.post("/discover-superpower")
async def discover_superpower():
    try:
        new_superpower = await discover_new_superpowers()
        return {"superpower": new_superpower}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Superpower discovery failed: " + str(e))

# Endpoint pour effectuer l'auto-amélioration de Jarvis
@app.post("/auto-improvement")
async def auto_improvement():
    try:
        patch = await generate_and_test_patch()
        return {"patch": patch}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Auto-improvement failed: " + str(e))
