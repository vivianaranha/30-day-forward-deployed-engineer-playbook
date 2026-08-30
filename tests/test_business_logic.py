from backend.app.business_logic import classify_category,estimate_priority,recommend_team
def test_auth(): assert classify_category("Login issue","User cannot sign in")=="authentication"
def test_network(): assert classify_category("High network latency","Multiple users impacted")=="network"
def test_critical(): assert estimate_priority("Outage","Production down for all users")=="critical"
def test_team(): assert recommend_team("billing")=="Billing Support"
