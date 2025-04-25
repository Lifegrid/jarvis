from transformers import pipeline
import logging

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_main_content(html: str) -> str:
    try:
        # On pourrait améliorer ce parseur plus tard
        start = html.find("<p>")
        end = html.find("</p>", start)
        text = html[start:end].replace("<p>", "").replace("</p>", "")
        if not text or len(text) < 20:
            text = html[:1000]  # fallback brut
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        logging.error(f"[Erreur résumé] {str(e)}")
        return "[Erreur résumé] " + str(e)
