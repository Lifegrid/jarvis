# autonomy/opportunity_detector.py

from datetime import datetime

def detect_opportunities(profile):
    """
    Détecte des opportunités d'action autonomes en fonction de l'heure, du jour ou du profil.
    """
    now = datetime.now()
    weekday = now.weekday()

    opportunities = []

    if weekday == 0:
        opportunities.append("Planifier la semaine")

    if now.hour == 9:
        opportunities.append("Analyser les emails professionnels")

    if "scraping" in profile.get("objectif", ""):
        opportunities.append("Lancer le scraping automatisé")

    return opportunities
