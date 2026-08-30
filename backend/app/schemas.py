from __future__ import annotations
from pydantic import BaseModel, Field

class TicketRequest(BaseModel):
    ticket_id: str = Field(min_length=1)
    subject: str = Field(min_length=3)
    description: str = Field(min_length=5)
    customer_tier: str = "standard"

class TicketAnalysis(BaseModel):
    ticket_id: str
    category: str
    priority: str
    summary: str
    recommended_team: str
    confidence: float
    explanation: str

class FeedbackRequest(BaseModel):
    ticket_id: str
    accepted: bool
    comment: str = ""
