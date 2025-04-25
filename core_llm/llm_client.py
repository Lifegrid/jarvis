import requests

LM_STUDIO_API_URL = "http://192.168.1.9:1234/v1/chat/completions"
MODEL_NAME = "openchat-3.5-0106"

# Prompt système enrichi
JARVIS_SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "Tu es Jarvis, une IA personnelle locale intelligente, fluide, proactive et utile.\n"
        "Tu parles à Jérémie avec clarté, concision et personnalité.\n"
        "Tu es capable de mémoire implicite sur les 10 derniers messages.\n"
        "Tu proposes des idées, reformules, corriges, et réponds toujours de manière utile et synthétique.\n"
        "Tu peux analyser les intentions (comme \"je vais manger\", \"ouvre Chrome\") et les fichiers ou liens.\n"
        "Utilise des émojis si pertinent."
    )
}

def query_llm(messages: list[dict[str, str]]) -> str:
    full_messages = [JARVIS_SYSTEM_PROMPT] + messages

    payload = {
        "model": MODEL_NAME,
        "messages": full_messages,
        "temperature": 0.7,
        "max_tokens": 512
    }

    try:
        response = requests.post(LM_STUDIO_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"❌ Erreur LLM local : {str(e)}"
    except (KeyError, IndexError):
        return "❌ Erreur : Réponse inattendue du LLM"

ask_llm = query_llm
