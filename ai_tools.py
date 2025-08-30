from transformers import pipeline

summarizer = pipeline("summarization")
tagger = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def summarize_note(text):
    return summarizer(text[:1000])[0]["summary_text"]

def tag_note(text):
    labels = ["work", "personal", "urgent", "idea", "project"]
    result = tagger(text[:1000], candidate_labels=labels)
    return [label for label, score in zip(result["labels"], result["scores"]) if score > 0.5]
         
