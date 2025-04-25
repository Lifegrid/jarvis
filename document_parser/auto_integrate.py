import os

def auto_ingest_documents():
    documents_path = "data/documents"
    os.makedirs(documents_path, exist_ok=True)
    # Extension future : intégrer automatiquement tous les fichiers texte
    return