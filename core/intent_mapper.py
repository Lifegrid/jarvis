from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

# Liste des intentions connues
INTENTIONS = {
    "chercher": [
        "recherche", "trouve", "peux-tu chercher", "va sur internet", "analyse ce lien", "explore"
    ],
    "résumer": [
        "résume", "fais un résumé", "analyse ce document", "explique ce fichier", "synthétise"
    ],
    "planifier": [
        "prévois", "organise", "crée un planning", "ajoute dans l'agenda", "programme", "plan"
    ],
    "exécuter": [
        "ouvre", "lance", "exécute", "démarre", "run ce code", "terminal"
    ],
    "coder": [
        "génère un script", "écris du code", "montre un exemple", "fais une fonction", "programme"
    ],
    "parler": [
        "dis-moi", "explique-moi", "que penses-tu", "réponds", "raconte-moi"
    ],
    "analyser": [
        "vérifie", "analyse", "scrute", "scanne", "audite"
    ],
    "créer": [
        "fabrique", "construis", "génère", "dessine", "invente"
    ]
}

def detect_intention(message: str, score_threshold=0.6):
    input_embedding = model.encode(message, convert_to_tensor=True)

    best_match = None
    best_score = 0.0

    for intention, phrases in INTENTIONS.items():
        for phrase in phrases:
            phrase_embedding = model.encode(phrase, convert_to_tensor=True)
            score = util.pytorch_cos_sim(input_embedding, phrase_embedding).item()
            if score > best_score:
                best_score = score
                best_match = intention

    if best_score >= score_threshold:
        return {
            "intention": best_match,
            "score": round(best_score, 3)
        }
    else:
        return {
            "intention": "inconnue",
            "score": round(best_score, 3)
        }

# Test CLI
if __name__ == "__main__":
    test_msg = "Tu peux me résumer ce document ?"
    result = detect_intention(test_msg)
    print(f"Message : {test_msg}\n→ Intention détectée : {result}")
