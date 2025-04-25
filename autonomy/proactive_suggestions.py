# suggestion_engine/proactive_suggestions.py

def generate_suggestions(profile):
    """
    Suggère proactivement des actions ou idées à l'utilisateur selon son profil.
    """
    suggestions = []

    if "crypto" in profile.get("passions", ""):
        suggestions.append("Souhaitez-vous consulter les tendances crypto aujourd'hui ?")

    if "organisation" in profile.get("objectif", ""):
        suggestions.append("Je peux vous aider à organiser vos tâches de la journée.")

    if profile.get("travail") == "au Crazy Horse":
        suggestions.append("Besoin de vérifier les horaires ou d'envoyer un message ?")

    return suggestions
