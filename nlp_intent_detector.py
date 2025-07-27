import spacy

nlp = spacy.load("ar_core_news_sm")

def detect_intent(text):
    doc = nlp(text)
    # Simple keyword-based intent detection
    if any(word in text for word in ["طلب", "أريد", "order"]):
        return "place_order"
    elif any(word in text for word in ["شكوى", "مشكلة", "complaint"]):
        return "complaint"
    return "general_query"