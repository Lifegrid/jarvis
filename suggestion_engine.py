import random
import json
from datetime import datetime

PROFILE_PATH = "memory_engine/user_profile.json"
MEMORY_PATH = "memory_engine/active_memory.json"


def load_profile():
    try:
        with open(PROFILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def load_memory():
    try:
        with open(MEMORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def suggest_actions():
    profile = load_profile()
    memory = load_memory()

    prénom = profile.get("prénom", "ami")
    travail = profile.get("travail", "ton domaine")
    passions = profile.get("passions", "la technologie")
    objectif = profile.get("objectif", "explorer l'IA")

    suggestions = [
        f"Tu veux que je t’aide à avancer sur ton projet d’IA personnelle ?",
        f"Je peux te faire un point rapide sur l’actu crypto ou IA si tu veux.",
        f"Souhaites-tu que je planifie une session de travail ce soir pour coder un module ?",
        f"Je peux t’ouvrir un doc pour noter tes idées du moment.",
        f"Besoin de consulter les dernières infos liées à {passions} ?"
    ]

    now = datetime.now().hour
    if now < 10:
        suggestions.append("Je peux t’aider à organiser ta journée dès maintenant.")
    elif now > 21:
        suggestions.append("Tu veux que je t’aide à résumer ce que tu as fait aujourd’hui ?")

    return f"Tu t'appelles {prénom}, tu travailles {travail}, tu es passionné par {passions}. {random.choice(suggestions)}"


if __name__ == "__main__":
    print(suggest_actions())
