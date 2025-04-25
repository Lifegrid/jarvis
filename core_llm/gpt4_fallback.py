# core_llm/gpt4_fallback.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_gpt4(messages, temperature=0.7):
    """
    Interroge GPT-4 via l’API OpenAI en cas de fallback.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[ERREUR GPT-4] {e}"
