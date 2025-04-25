import requests

# Configuration de l'API locale LM Studio
LM_STUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "openchat-3.5-0106"

# Prompt système enrichi pour Jarvis
JARVIS_SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "Tu es Jarvis, une intelligence artificielle personnelle locale, proactive, créative et utile.\n"
        "Tu parles à Jérémie avec clarté, concision et une touche de personnalité.\n"
        "Tu es capable de mémoire contextuelle sur les derniers messages.\n"
        "Tu proposes des idées, analyses les intentions, aides à coder, corriges des erreurs, et t'auto-améliores.\n"
        "Utilise des émojis si pertinent pour rendre la communication plus fluide."
    )
}

def ask_llm(messages: list[dict[str, str]]) -> str:
    """
    Interroge le LLM local pour générer une réponse contextuelle basée sur la conversation.
    """
    full_messages = [JARVIS_SYSTEM_PROMPT] + messages

    payload = {
        "model": MODEL_NAME,
        "messages": full_messages,
        "temperature": 0.7,  # Créativité équilibrée
        "max_tokens": 512
    }

    try:
        response = requests.post(LM_STUDIO_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"❌ Erreur de communication avec LLM local : {str(e)}"
    except (KeyError, IndexError):
        return "❌ Erreur : réponse inattendue du LLM."

def generate_code_from_prompt(prompt: str) -> str:
    """
    Génère du code à partir d'une simple instruction utilisateur.
    Utilisé pour l'auto-amélioration de Jarvis.
    """
    payload = {
        "model": MODEL_NAME,
        "messages": [
            JARVIS_SYSTEM_PROMPT,
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,  # Baisse pour obtenir du code fiable
        "max_tokens": 1024
    }

    try:
        response = requests.post(LM_STUDIO_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"❌ Erreur de communication avec LLM local : {str(e)}"
    except (KeyError, IndexError):
        return "❌ Erreur : réponse inattendue du LLM."
