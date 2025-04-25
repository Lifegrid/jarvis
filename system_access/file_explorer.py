import os
from web_scraper.content_summarizer import summarize_content
from web_scraper.source_vectorizer import store_vector

def explore_and_store(folder_path="docs"):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".txt", ".md", ".pdf")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        print(f"📄 Analyse de : {path}")
                        summary = summarize_content(content)
                        store_vector(path, summary)
                        print(f"✅ Stocké : {path}")
                except Exception as e:
                    print(f"❌ Erreur sur {file} : {e}")
