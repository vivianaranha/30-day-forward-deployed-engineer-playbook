from backend.app.integrations import MockTicketSystem
def test_update():
 s=MockTicketSystem(); r=s.update_ticket("T-1",{"priority":"high"}); assert r["status"]=="updated"; assert s.writes[0]["ticket_id"]=="T-1"
