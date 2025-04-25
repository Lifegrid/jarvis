from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from main import generate_reply, process_uploaded_file, analyze_user_message, get_bilan
import glob
import os
import json

app = FastAPI()

# Autoriser le frontend à se connecter à l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:3000"] pour être plus strict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(message: str = Form(...), conversation_id: str = Form(None)):
    """
    Endpoint principal pour recevoir un message utilisateur
    et générer une réponse depuis Jarvis.
    """
    reply = generate_reply(message, conversation_id)
    return {"reply": reply}

@app.post("/upload")
async def upload(file: UploadFile = File(...), conversation_id: str = Form(None)):
    """
    Endpoint pour uploader un fichier et le résumer dans la conversation.
    """
    summary = await process_uploaded_file(file, conversation_id)
    return {"reply": summary}

@app.get("/bilan")
async def bilan():
    """
    Endpoint pour générer un bilan quotidien intelligent.
    """
    bilan = await get_bilan()
    return {"bilan": bilan}

@app.get("/conversations")
async def list_conversations():
    """
    Liste toutes les conversations existantes.
    """
    conversation_files = glob.glob("conversations/*.json")
    conversations = []
    for file_path in conversation_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)
                if history:
                    first_message = history[0].get("text", "Sans titre")
                else:
                    first_message = "Sans titre"
                conversation_id = os.path.splitext(os.path.basename(file_path))[0]
                conversations.append({"id": conversation_id, "title": first_message})
        except Exception:
            continue
    return JSONResponse(content={"conversations": conversations})

@app.get("/conversation/{conversation_id}")
async def get_conversation(conversation_id: str):
    """
    Récupère tous les messages d'une conversation spécifique.
    """
    filepath = os.path.join("conversations", f"{conversation_id}.json")
    if not os.path.exists(filepath):
        return JSONResponse(content={"messages": []})

    with open(filepath, "r", encoding="utf-8") as f:
        messages = json.load(f)
    return JSONResponse(content={"messages": messages})
