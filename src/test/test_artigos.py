from starlette.testclient import TestClient

from src.server import app

client = TestClient(app)


def test_status_code_get_articles():
    resp = client.get('/articles/')
    assert resp.status_code == 200
