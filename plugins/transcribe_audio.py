import whisper
import os

model = whisper.load_model("base")  # 'base', 'small', 'medium', 'large'

def transcribe_audio(path: str) -> str:
    """Transcrit un fichier audio en texte via Whisper"""
    if not os.path.exists(path):
        return "[Erreur] Fichier audio introuvable."

    try:
        print("[Jarvis] Transcription en cours...")
        result = model.transcribe(path, language="fr")
        return result["text"].strip()
    except Exception as e:
        return f"[Erreur transcription] {str(e)}"

# Test CLI
if __name__ == "__main__":
    texte = transcribe_audio("data/audio/voix.mp3")
    print("Transcription :\n", texte)
