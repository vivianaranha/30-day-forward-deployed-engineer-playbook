from time import perf_counter
from fastapi import FastAPI,HTTPException
from .schemas import TicketRequest,TicketAnalysis,FeedbackRequest
from .service import analyze_ticket
from .metrics import metrics_store
from .integrations import ticket_system
app=FastAPI(title="FDE Support Triage API",version="1.0.0")
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/analyze",response_model=TicketAnalysis)
def analyze(req:TicketRequest):
    start=perf_counter(); result=analyze_ticket(req); metrics_store.record_analysis((perf_counter()-start)*1000); return result
@app.post("/tickets/{ticket_id}/apply")
def apply_recommendation(ticket_id:str,analysis:TicketAnalysis):
    if ticket_id!=analysis.ticket_id: raise HTTPException(status_code=400,detail="Ticket ID mismatch")
    return ticket_system.update_ticket(ticket_id,{"category":analysis.category,"priority":analysis.priority,"recommended_team":analysis.recommended_team,"summary":analysis.summary})
@app.post("/feedback")
def feedback(req:FeedbackRequest): metrics_store.record_feedback(req.accepted); return {"status":"recorded"}
@app.get("/metrics")
def metrics(): return metrics_store.snapshot()
