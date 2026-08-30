from fastapi.testclient import TestClient
from backend.app.main import app
client=TestClient(app)
def test_health(): assert client.get("/health").json()["status"]=="ok"
def test_analyze():
 r=client.post("/analyze",json={"ticket_id":"T-100","subject":"Invoice total incorrect","description":"Customer reports duplicate billing charges.","customer_tier":"gold"}); assert r.status_code==200; assert r.json()["category"]=="billing"
def test_invalid(): assert client.post("/analyze",json={"ticket_id":"","subject":"x","description":"bad"}).status_code==422
