import os
import json
from datetime import datetime

CONVERSATION_DIR = "conversations"
os.makedirs(CONVERSATION_DIR, exist_ok=True)

def get_all_conversations():
    conversations = []
    for filename in os.listdir(CONVERSATION_DIR):
        if filename.endswith(".json"):
            path = os.path.join(CONVERSATION_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                conversations.append({
                    "id": filename.replace(".json", ""),
                    "title": data.get("title", "Nouvelle conversation"),
                    "timestamp": data.get("timestamp")
                })
    return sorted(conversations, key=lambda x: x["timestamp"], reverse=True)

def get_conversation(convo_id):
    path = os.path.join(CONVERSATION_DIR, f"{convo_id}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_message(convo_id, message):
    convo = get_conversation(convo_id)
    if convo is None:
        convo = {
            "id": convo_id,
            "title": f"Conversation {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            "timestamp": datetime.now().isoformat(),
            "messages": []
        }
    convo["messages"].append(message)
    convo["timestamp"] = datetime.now().isoformat()
    with open(os.path.join(CONVERSATION_DIR, f"{convo_id}.json"), "w", encoding="utf-8") as f:
        json.dump(convo, f, ensure_ascii=False, indent=2)

def rename_conversation(convo_id, new_title):
    convo = get_conversation(convo_id)
    if convo:
        convo["title"] = new_title
        with open(os.path.join(CONVERSATION_DIR, f"{convo_id}.json"), "w", encoding="utf-8") as f:
            json.dump(convo, f, ensure_ascii=False, indent=2)
        return True
    return False

def delete_conversation(convo_id):
    path = os.path.join(CONVERSATION_DIR, f"{convo_id}.json")
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
