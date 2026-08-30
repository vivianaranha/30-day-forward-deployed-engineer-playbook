class MockTicketSystem:
    def __init__(self): self.writes=[]
    def update_ticket(self,ticket_id,fields):
        record={"ticket_id":ticket_id,"fields":fields}; self.writes.append(record)
        return {"status":"updated",**record}
ticket_system=MockTicketSystem()
