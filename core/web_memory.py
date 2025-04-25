# core/web_memory.py

import os
import json
import hashlib

WEB_MEMORY_DIR = "web_memory"
os.makedirs(WEB_MEMORY_DIR, exist_ok=True)

def _hash_query(query: str) -> str:
    """
    Génère un identifiant unique pour chaque requête web.
    """
    return hashlib.sha256(query.encode("utf-8")).hexdigest()

def store_web_memory(query: str, summary: str):
    """
    Sauvegarde une synthèse d'une recherche web.
    """
    query_hash = _hash_query(query)
    filepath = os.path.join(WEB_MEMORY_DIR, f"{query_hash}.json")

    data = {
        "query": query,
        "summary": summary
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def search_web_memory(query: str) -> str | None:
    """
    Vérifie si un résumé existe déjà pour cette requête.
    """
    query_hash = _hash_query(query)
    filepath = os.path.join(WEB_MEMORY_DIR, f"{query_hash}.json")

    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("summary")
        except Exception:
            return None

    return None
