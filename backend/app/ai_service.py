def summarize_ticket(subject,description):
    clean=" ".join(description.split())
    if len(clean)>160: clean=clean[:157]+"..."
    return f"{subject.strip()}: {clean}"

def confidence_for(category,priority):
    score=.78
    if category!="general": score+=.10
    if priority in {"high","critical"}: score+=.05
    return min(score,.95)

def explanation(category,priority):
    return f"The ticket was classified as '{category}' based on routing signals. Priority was estimated as '{priority}' from impact and urgency signals."
