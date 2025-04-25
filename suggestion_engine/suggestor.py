import random

def suggest_actions(profile: dict) -> list:
    suggestions = []

    if "crypto" in profile.get("passions", "").lower():
        suggestions.append("📈 Souhaitez-vous suivre les tendances crypto aujourd’hui ?")
    if "crazy horse" in profile.get("travail", "").lower():
        suggestions.append("🎭 Voulez-vous que je planifie votre préparation pour le Crazy Horse ?")
    if "ia" in profile.get("objectif", "").lower():
        suggestions.append("🤖 Vous voulez que je vous aide à avancer sur votre projet d’IA personnelle ?")
    
    if not suggestions:
        suggestions.append("🧠 Souhaitez-vous que je vous propose une tâche ou une idée pour aujourd’hui ?")
    
    return random.sample(suggestions, k=min(2, len(suggestions)))
