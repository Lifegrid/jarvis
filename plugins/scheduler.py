import dateparser
from datetime import datetime
import uuid

def extract_schedule(message: str) -> dict:
    """Détecte une date ou heure dans une phrase, retourne un événement"""
    parsed = dateparser.parse(message, languages=["fr"])
    if not parsed:
        return {"status": "fail", "message": "Aucune date trouvée."}

    event = {
        "id": str(uuid.uuid4()),
        "message": message,
        "datetime": parsed.strftime("%Y-%m-%d %H:%M:%S"),
        "timestamp": parsed.timestamp()
    }
    return {"status": "ok", "event": event}

# Test CLI
if __name__ == "__main__":
    result = extract_schedule("Préviens-moi demain à 9h d’envoyer l’email à Erika")
    print(result)
