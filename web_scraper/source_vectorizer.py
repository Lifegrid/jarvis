from chromadb import PersistentClient
from chromadb.utils import embedding_functions

# Nouveau client Chroma
client = PersistentClient(path=".jarvis_vector_db")

# Fonction d'embedding
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Récupère ou crée une collection
collection = client.get_or_create_collection(name="jarvis_docs", embedding_function=embedder)

def store_vector(source: str, text: str):
    """Stocke un document vectorisé"""
    try:
        collection.add(
            documents=[text],
            metadatas=[{"source": source}],
            ids=[source]
        )
    except Exception as e:
        print(f"[store_vector] Erreur : {e}")

def search_memory(query: str, top_k: int = 5):
    """Recherche contextuelle dans la mémoire vectorielle"""
    try:
        results = collection.query(query_texts=[query], n_results=top_k)
        return results["documents"][0]
    except Exception as e:
        print(f"[search_memory] Erreur : {e}")
        return []
