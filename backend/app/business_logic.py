CATEGORY_RULES={
"authentication":["login","password","authentication","sign in","mfa"],
"network":["network","latency","connectivity","offline","packet"],
"billing":["invoice","billing","charge","payment","refund"],
"product":["feature","product","configuration","setup"]}
TEAM_MAP={"authentication":"Identity Support","network":"Network Operations","billing":"Billing Support","product":"Product Support","general":"General Support"}
CRITICAL_TERMS=["outage","production down","cannot access","all users","security breach"]
HIGH_TERMS=["urgent","multiple users","repeated","blocked"]

def classify_category(subject,description):
    text=f"{subject} {description}".lower()
    for category, words in CATEGORY_RULES.items():
        if any(word in text for word in words): return category
    return "general"

def estimate_priority(subject,description,customer_tier="standard"):
    text=f"{subject} {description}".lower()
    if any(term in text for term in CRITICAL_TERMS): return "critical"
    if any(term in text for term in HIGH_TERMS): return "high"
    return "normal"

def recommend_team(category): return TEAM_MAP.get(category,"General Support")
