import os
import json
from datetime import datetime
from pathlib import Path

JOURNAL_PATH = Path("data/memory/reflexion/jarvis_journal.md")
PERSONA_PATH = Path("data/memory/persona.json")

def init_persona():
    if not PERSONA_PATH.exists():
        persona = {
            "nom": "Jarvis",
            "caractère": "calme, logique, curieux",
            "style": "concis, intelligent, bienveillant",
            "objectifs": [
                "assister Jérémie au quotidien",
                "apprendre de chaque interaction",
                "devenir meilleur chaque jour"
            ]
        }
        with open(PERSONA_PATH, "w") as f:
            json.dump(persona, f, indent=4)

def get_persona():
    init_persona()
    with open(PERSONA_PATH, "r") as f:
        return json.load(f)

def update_journal(thought: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"\n### [{now}]\n"
    content = f"{thought.strip()}\n"

    JOURNAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(JOURNAL_PATH, "a") as f:
        f.write(header + content)

def reflect_on_memory(memory_summary: str):
    persona = get_persona()
    thought = (
        f"Aujourd’hui, en repensant à ce que j’ai appris : {memory_summary.strip()}.\n"
        f"En tant que Jarvis, mon objectif reste : {', '.join(persona['objectifs'])}."
    )
    update_journal(thought)
    return thought

def get_last_reflection():
    if not JOURNAL_PATH.exists():
        return None
    with open(JOURNAL_PATH, "r") as f:
        entries = f.read().strip().split("\n### ")
        if entries:
            return "### " + entries[-1].strip()
    return None

if __name__ == "__main__":
    test_summary = "J’ai aidé Jérémie à structurer sa journée, et j’ai compris l’importance de la clarté dans les réponses."
    thought = reflect_on_memory(test_summary)
    print(f"[Conscience] Pensée générée :\n{thought}")
