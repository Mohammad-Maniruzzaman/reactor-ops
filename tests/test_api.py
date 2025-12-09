from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """
    Ensure the orchestrator is alive.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "operational", "service": "reactor-core"}

def test_bedrock_latency():
    """
    TODO: Integration test for AWS Bedrock latency.
    Must ensure < 2s response time for RAG generation.
    """
    pass
