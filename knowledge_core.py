import json
import os

KNOWLEDGE_FILE = "memory/knowledge.json"

def load_knowledge():
    if not os.path.exists(KNOWLEDGE_FILE):
        return {}
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_knowledge(data):
    with open(KNOWLEDGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def extract_facts(message: str) -> dict:
    # ⚠️ À améliorer avec NLP ou LLM plus tard
    facts = {}
    if "je m'appelle" in message.lower():
        parts = message.split("je m'appelle")
        if len(parts) > 1:
            name = parts[1].strip().split()[0]
            facts["nom_utilisateur"] = name
    if "ma femme s'appelle" in message.lower():
        parts = message.split("ma femme s'appelle")
        if len(parts) > 1:
            wife = parts[1].strip().split()[0]
            facts["conjointe"] = wife
    return facts

def memorize_facts(message: str):
    memory = load_knowledge()
    new_facts = extract_facts(message)
    memory.update(new_facts)
    save_knowledge(memory)

def inject_facts_into_prompt() -> str:
    memory = load_knowledge()
    lines = [f"{k.replace('_', ' ').capitalize()} : {v}" for k, v in memory.items()]
    return "\n".join(lines) if lines else ""
