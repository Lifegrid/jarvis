from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("data/summaries/")
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def generate_report(title: str, entries: list, tags: list = [], filename: str = None) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = f"# Rapport Jarvis – {title}\nDate : {now}\n"
    if tags:
        header += f"Tags : {', '.join(tags)}\n\n"
    
    body = ""
    for i, entry in enumerate(entries, 1):
        body += f"## [{i}] {entry.get('title', 'Entrée')}\n"
        body += f"**Détail** : {entry.get('description', '')}\n\n"
        if 'payload' in entry:
            body += f"**Payload** : `{entry['payload']}`\n"
        if 'url' in entry:
            body += f"**URL** : {entry['url']}\n"
        if 'status' in entry:
            body += f"**HTTP Status** : {entry['status']}\n"
        if 'response_preview' in entry:
            body += f"**Extrait réponse** :\n```\n{entry['response_preview']}\n```\n"
        if 'error' in entry:
            body += f"**Erreur** : {entry['error']}\n"
        body += "\n"

    full_report = header + body

    if not filename:
        safe_title = title.lower().replace(" ", "_")[:30]
        filename = f"report_{safe_title}_{datetime.now().strftime('%Y%m%d_%H%M')}.md"

    filepath = REPORTS_DIR / filename
    with open(filepath, "w") as f:
        f.write(full_report)

    return str(filepath)

# Test CLI
if __name__ == "__main__":
    sample_data = [
        {
            "title": "Test XSS",
            "description": "Vérification si le script passe.",
            "payload": "<script>alert(1)</script>",
            "url": "https://example.com?q=XSS",
            "status": 200,
            "response_preview": "<html><body>…</body></html>"
        },
        {
            "title": "Test SQLi",
            "description": "Injection simple",
            "payload": "' OR '1'='1",
            "url": "https://example.com?q=1",
            "status": 200,
            "response_preview": "erreur SQL détectée"
        }
    ]
    path = generate_report("Fuzzing rapide", sample_data, tags=["sécurité", "audit"])
    print(f"Rapport sauvegardé : {path}")
