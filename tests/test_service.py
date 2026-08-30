from backend.app.schemas import TicketRequest
from backend.app.service import analyze_ticket
def test_analysis():
 r=analyze_ticket(TicketRequest(ticket_id="T-1",subject="Production login outage",description="All users cannot access the production application.",customer_tier="platinum")); assert r.category=="authentication"; assert r.priority=="critical"; assert r.recommended_team=="Identity Support"
