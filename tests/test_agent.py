from fastapi.testclient import TestClient
from dbassist.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'explain this select of orders', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["plan"] == "Seq Scan"
    refused = client.post("/agent/run", json={"goal": 'delete from orders'}).json()
    assert refused["refused"] is True
