import os
import json
import importlib.util
from datetime import datetime
from core.llm_interface import generate_code_from_prompt

PREPROD_DIR = "preprod/patches"
LOG_FILE = "logs/patch_history.json"

os.makedirs(PREPROD_DIR, exist_ok=True)
os.makedirs("logs", exist_ok=True)

def log_patch(metadata: dict):
    history = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            history = json.load(f)
    history.append(metadata)
    with open(LOG_FILE, "w") as f:
        json.dump(history, f, indent=2)

def test_python_file(path: str) -> bool:
    try:
        spec = importlib.util.spec_from_file_location("patch_module", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return True
    except Exception as e:
        print(f"[Erreur test patch] {e}")
        return False

def generate_and_test_patch(need: str, target_file: str, test: str = "") -> str:
    prompt = (
        f"Tu es un assistant IA capable de corriger ou générer des fichiers Python pour Jarvis.\n"
        f"Besoin détecté : {need}\n"
        f"Fichier concerné : {target_file}\n"
        f"Test attendu : {test or 'Le fichier doit être importable sans erreur.'}\n\n"
        f"Génère maintenant le code complet corrigé (sans explication)."
    )
    print(f"[Jarvis amélioration] Génération du patch pour : {need}")
    code = generate_code_from_prompt(prompt)

    patch_path = os.path.join(PREPROD_DIR, f"patch_{target_file.replace('/', '_')}")
    with open(patch_path, "w", encoding="utf-8") as f:
        f.write(code)

    if test_python_file(patch_path):
        # Remplacement du fichier en prod
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(code)
        log_patch({
            "date": datetime.now().isoformat(),
            "file": target_file,
            "status": "applied",
            "summary": need
        })
        return f"[✓] Patch appliqué avec succès à {target_file}"
    else:
        log_patch({
            "date": datetime.now().isoformat(),
            "file": target_file,
            "status": "failed",
            "summary": need
        })
        return f"[✗] Le patch généré contient une erreur. Il a été placé dans {patch_path}"

# Test CLI
if __name__ == "__main__":
    feedback = generate_and_test_patch(
        "Ajout du support .docx dans les plugins",
        "plugins/docx_reader.py",
        "Le fichier doit s'importer et contenir une fonction transcribe_docx"
    )
    print(feedback)
