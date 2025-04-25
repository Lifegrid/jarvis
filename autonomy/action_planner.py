# autonomy/action_planner.py

from datetime import datetime

def generate_action_plan(profile):
    """
    Génère une liste d'actions autonomes basées sur le profil utilisateur.
    """
    actions = []
    now = datetime.now()
    hour = now.hour

    if "IA personnelle" in profile.get("objectif", ""):
        actions.append("Continuer le projet IA personnelle")

    if hour < 10:
        actions.append("Vérifier les emails")
    if hour == 12:
        actions.append("Faire une pause déjeuner")
    if hour >= 18:
        actions.append("Faire un point sur les tâches de la journée")

    if "crypto" in profile.get("passions", ""):
        actions.append("Scraper les actus crypto")
    if "technologie" in profile.get("passions", ""):
        actions.append("Faire une veille technologique")

    return actions
