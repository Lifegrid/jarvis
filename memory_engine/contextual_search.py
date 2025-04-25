import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

embedder = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection("jarvis_docs", embedding_function=embedder)

def query_documents(question: str, k: int = 5):
    results = collection.query(
        query_texts=[question],
        n_results=k
    )
    return results["documents"][0] if results["documents"] else []
