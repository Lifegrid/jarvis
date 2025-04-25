import chromadb

client = chromadb.PersistentClient(path="memory/vectorstore")
collection = client.get_or_create_collection("knowledge")

def search_memory(query, top_k=3):
    results = collection.query(query_texts=[query], n_results=top_k)
    return results["documents"][0] if results and results["documents"] else []
