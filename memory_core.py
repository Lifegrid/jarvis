import os
import json
import hashlib
from sentence_transformers import SentenceTransformer
import chromadb

DB_DIR = "memory/vector_store"
COLLECTION_NAME = "jarvis_memories"

model = SentenceTransformer("all-MiniLM-L6-v2")
db = chromadb.PersistentClient(path=DB_DIR)
collection = db.get_or_create_collection(COLLECTION_NAME)

def embed_text(text):
    return model.encode(text).tolist()

def store_memory(text, metadata=None):
    metadata = metadata or {}
    memory_id = hashlib.sha256(text.encode()).hexdigest()
    embedding = embed_text(text)
    collection.add(documents=[text], embeddings=[embedding], metadatas=[metadata], ids=[memory_id])

def query_memory(query, n_results=5):
    embedding = embed_text(query)
    results = collection.query(query_embeddings=[embedding], n_results=n_results)
    return results.get("documents", [[]])[0] if results else []

def summarize_memories():
    all_docs = collection.get()["documents"]
    return "\n".join(all_docs[:5]) if all_docs else "(Aucune mémoire enregistrée)"

