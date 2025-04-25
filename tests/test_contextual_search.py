from memory_engine.contextual_search import query_documents

print("🔍 Recherche dans les documents :")
question = "Quels sont les objectifs du projet Jarvis ?"
results = query_documents(question)

if results:
    for i, (doc, meta) in enumerate(results, 1):
        print(f"\nRésultat {i}:")
        print("📄 Source :", meta.get("source", "inconnue"))
        print("📖 Extrait :", doc[:300])
else:
    print("❌ Aucun résultat trouvé.")
