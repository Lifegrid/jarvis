import chromadb
from datetime import datetime
import os

# Dossier de stockage local pour ChromaDB
CHROMA_DIR = "data/memory"
os.makedirs(CHROMA_DIR, exist_ok=True)

client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection(name="jarvis_memory")

def store_memory_snapshot(content: str, source: str = "chat", metadata: dict = None, category: str = "général"):
    """Stocke un souvenir dans la base vectorielle Jarvis"""
    if not metadata:
        metadata = {}

    now = datetime.now().isoformat()
    memory_id = f"memory_{now.replace(':', '-')}"
    metadata.update({
        "source": source,
        "timestamp": now,
        "category": category,
    })

    collection.add(
        documents=[content],
        metadatas=[metadata],
        ids=[memory_id]
    )

def search_memory(query: str, n_results: int = 5):
    """Recherche sémantique dans les souvenirs"""
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas"]
    )

    return list(zip(results["documents"][0], results["metadatas"][0]))
