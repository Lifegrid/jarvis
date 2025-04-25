# tests/test_intent_mapper.py

from core_llm.intent_mapper import detect_intent

def test_intents():
    prompts = [
        "Ouvre Google Chrome",
        "Crée un fichier texte nommé notes.txt",
        "Peux-tu me générer du code Python ?",
        "Utilise le plugin météo",
        "Quelle est la capitale de la Suisse ?"
    ]

    for prompt in prompts:
        intent = detect_intent(prompt)
        print(f"[{prompt}]  →  🧭 Intention détectée : {intent}")

if __name__ == "__main__":
    test_intents()
