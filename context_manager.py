import os
import json
from collections import defaultdict

CONTEXT_PATH = "context"

if not os.path.exists(CONTEXT_PATH):
    os.makedirs(CONTEXT_PATH)

_sessions = defaultdict(list)


def update_context(convo_id: str, message: str, from_user: bool):
    entry = {"role": "user" if from_user else "assistant", "content": message}
    _sessions[convo_id].append(entry)
    save_context(convo_id)


def get_context(convo_id: str):
    if convo_id in _sessions:
        return _sessions[convo_id][-10:]  # dernier échange
    load_context(convo_id)
    return _sessions[convo_id][-10:]


def save_context(convo_id: str):
    with open(os.path.join(CONTEXT_PATH, f"{convo_id}.json"), "w", encoding="utf-8") as f:
        json.dump(_sessions[convo_id], f, ensure_ascii=False, indent=2)


def load_context(convo_id: str):
    path = os.path.join(CONTEXT_PATH, f"{convo_id}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            _sessions[convo_id] = json.load(f)


# Pour récupérer le dernier sujet de discussion

def get_last_user_message(convo_id: str) -> str:
    context = _sessions.get(convo_id, [])
    for msg in reversed(context):
        if msg["role"] == "user":
            return msg["content"]
    return ""


def get_last_jarvis_reply(convo_id: str) -> str:
    context = _sessions.get(convo_id, [])
    for msg in reversed(context):
        if msg["role"] == "assistant":
            return msg["content"]
    return ""


def clear_context(convo_id: str):
    _sessions[convo_id] = []
    save_context(convo_id)
