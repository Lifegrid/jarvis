# core_llm/llm_stub.py

def mock_chat_response(prompt: str) -> str:
    if "comment tu t'appelles" in prompt.lower():
        return "Je suis Jarvis, ton assistant personnel !"
    elif "blague" in prompt.lower():
        return "Pourquoi les développeurs n’aiment pas la nature ? Parce qu’il y a trop de bugs ! 🐛"
    elif "gratins" in prompt.lower() or "chauffe" in prompt.lower():
        return "En général, un gratin se réchauffe 15-20 minutes à 180°C dans un four préchauffé."
    else:
        return "Hello! How can I help you today? If you have any questions or need assistance with something, feel free to ask."
