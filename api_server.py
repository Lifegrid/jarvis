from fastapi import FastAPI, UploadFile, Form, HTTPException
from main import generate_reply, process_uploaded_file, analyze_user_message, get_bilan
import os
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str
    conversation_id: str

@app.post("/chat")
async def chat(message: Message):
    try:
        # Générer une réponse pour la conversation
        reply = generate_reply(message.conversation_id, message.text)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/upload-file")
async def upload_file(conversation_id: str, file: UploadFile):
    try:
        # Traiter un fichier téléchargé
        result = process_uploaded_file(conversation_id, file)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {str(e)}")

@app.get("/bilan")
async def bilan():
    try:
        # Retourner le bilan quotidien basé sur les souvenirs web et autres sources
        return {"bilan": get_bilan()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while generating the bilan: {str(e)}")

@app.get("/discover-superpower")
async def discover_superpower():
    try:
        # Découverte autonome des super-pouvoirs
        # (pour l'instant, on envoie une proposition fictive pour les tests)
        superpowers = [
            "Améliorer l'IA pour des décisions plus intelligentes",
            "Ajouter un plugin pour automatiser les tâches administratives",
            "Créer un mode 'sécurité offensive' pour tester des applications"
        ]
        return {"superpowers": superpowers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while discovering superpowers: {str(e)}")

@app.post("/analyze")
async def analyze(message: Message):
    try:
        # Analyser un message utilisateur pour comprendre son intention
        result = analyze_user_message(message.text)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while analyzing the message: {str(e)}")

# Ajouter d'autres routes si nécessaire pour de futurs développements

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
