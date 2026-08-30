from .schemas import TicketRequest,TicketAnalysis
from .business_logic import classify_category,estimate_priority,recommend_team
from .ai_service import summarize_ticket,confidence_for,explanation

def analyze_ticket(req:TicketRequest)->TicketAnalysis:
    category=classify_category(req.subject,req.description)
    priority=estimate_priority(req.subject,req.description,req.customer_tier)
    return TicketAnalysis(ticket_id=req.ticket_id,category=category,priority=priority,summary=summarize_ticket(req.subject,req.description),recommended_team=recommend_team(category),confidence=confidence_for(category,priority),explanation=explanation(category,priority))
