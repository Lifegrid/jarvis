import datetime

def suggest_actions(profile):
    now = datetime.datetime.now()
    hour = now.hour
    weekday = now.strftime('%A')

    suggestions = []

    if hour < 9:
        suggestions.append("Tu veux que je t'aide à planifier ta journée ?")
    elif hour < 12:
        suggestions.append("Et si on faisait un point sur tes projets en cours ?")
    elif hour < 18:
        suggestions.append("Souhaites-tu que je scrute les dernières actus crypto ?")
    else:
        suggestions.append("Tu veux que je résume ce que tu as accompli aujourd'hui ?")

    if weekday in ['Saturday', 'Sunday']:
        suggestions.append("Tu veux te détendre ? Je peux te recommander un film ou un article sympa.")

    if profile.get("objectif") == "créer une IA personnelle":
        suggestions.append("Souhaites-tu que je travaille sur une fonction autonome aujourd’hui ?")

    return suggestions
