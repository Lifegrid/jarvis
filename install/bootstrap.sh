#!/bin/bash

echo "=== [ JARVIS V∞ BOOTSTRAP - INITIALISATION GLOBALE ] ==="

### 1. Création des dossiers clés
echo "[+] Création de l'arborescence des dossiers..."

mkdir -p core modules security plugins data/{logs,memory,embeddings,raw,snapshots,summaries,memory/reflexion} \
         dev preprod prod install ui

touch data/memory/daily_bilan.json
touch data/memory/persona.json
touch data/memory/reflexion/jarvis_journal.md
touch plugins/plugin.json

### 2. Création des fichiers de base
echo "[+] Création des fichiers essentiels..."

cat <<EOF > requirements.txt
fastapi
uvicorn
pydantic
httpx
requests
openai
transformers
sentence-transformers
chromadb
langdetect
python-multipart
pytesseract
easyocr
opencv-python
whisper
pyttsx3
elevenlabs
SpeechRecognition
numpy
scikit-learn
pandas
tqdm
psutil
aiofiles
rich
pyyaml
Jinja2
pytest
docker
gitpython
EOF

### 3. Installation de l’environnement Python
echo "[+] Création de l’environnement virtuel Python..."

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

### 4. Téléchargement du backend ChromaDB
echo "[+] Initialisation de la base ChromaDB..."

python -c "import chromadb; chromadb.Client()"

### 5. Lancement de l’API
echo "[+] Lancement de l’API FastAPI (localhost:8000)..."

gnome-terminal -- uvicorn api_server:app --reload

### 6. Lancement du frontend (Next.js)
echo "[+] Lancement du frontend (localhost:3000)..."

cd ui
npm install
npm run dev

### 7. Fin
echo "=== Jarvis V∞ est prêt ! API sur : http://localhost:8000 | UI sur : http://localhost:3000 ==="
