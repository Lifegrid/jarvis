import os
from datetime import datetime
from web_research import needs_web_search, autonomous_web_research
from core_llm.llm_client import ask_llm
from memory_engine.memory_utils import store_memory_snapshot
from system_access.intent_mapper import detect_intent_and_execute, detect_implicit_intent, contains_url, extract_first_url
from bilan_engine import should_run_bilan, generate_daily_bilan
from web_scraper import smart_web_summary

profile = {
    "name": "Jérémie",
    "priorities": ["IA personnelle", "crypto", "technologie"],
    "routines": ["email", "pause", "bilan"]
}

def process_user_input(message: str) -> str:
    # ✔ Intent explicite d'action locale (ouvrir VSCode, cmd, etc)
    intent_check = [
        {"role": "system", "content": "Tu es un détecteur d'intention. Si l'utilisateur demande d'exécuter une action sur l'ordinateur (comme ouvrir un logiciel, un site, éteindre le PC...), réponds uniquement par 'SYSTEM'. Sinon, réponds 'CHAT'."},
        {"role": "user", "content": message}
    ]
    try:
        intent = ask_llm(intent_check).strip().upper()
    except Exception:
        intent = "CHAT"

    if intent == "SYSTEM":
        return detect_intent_and_execute(message)

    # ✔ Intent implicite (analyse lien, contexte resto, etc)
    implicit = detect_implicit_intent(message)
    if implicit == "analyse_lien" and contains_url(message):
        url = extract_first_url(message)
        summary = smart_web_summary(url)
        store_memory_snapshot("web_summary", {"user": message, "jarvis": summary})
        return summary

    if implicit == "suggestion_restaurant":
        return "Souhaitez-vous que je vous recommande un cocktail ou un menu en lien avec l'endroit mentionné ?"

    if needs_web_search(message):
        web_summary = autonomous_web_research(message)
        store_memory_snapshot("web_summary", web_summary)
        return web_summary

    if should_run_bilan():
        bilan = generate_daily_bilan()
        store_memory_snapshot("daily_bilan", bilan)

    # ✔ Réponse normale contextuelle
    messages = [
        {"role": "system", "content": "Tu es Jarvis, un assistant personnel intelligent et proactif, qui répond avec clarté, précision et style élégant à Jérémie."},
        {"role": "user", "content": message}
    ]
    response = ask_llm(messages)
    store_memory_snapshot("chat", {"user": message, "jarvis": response})
    return response

def get_suggestions() -> list[str]:
    hour = datetime.now().hour

    suggestions = []
    if 6 <= hour < 9:
        suggestions = ["Planifie ta journée", "Vérifie les actus IA", "Fais un point rapide"]
    elif 12 <= hour < 14:
        suggestions = ["Prends une pause", "Lis un article tech", "Résumé des mails"]
    elif 17 <= hour < 20:
        suggestions = ["Fais un bilan rapide", "Revue des tâches", "Check crypto"]
    else:
        suggestions = ["Pose-moi une question", "Découvre une nouveauté IA"]

    return suggestions
