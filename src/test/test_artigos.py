from starlette.testclient import TestClient

from src.server import app

client = TestClient(app)


def test_status_code_get_articles():
    """
    Testa se ao fazer uma requisição get para o endpoint /articles/ é retornado código 200
    """
    resp = client.get('/articles/')
    assert resp.status_code == 200


def test_buscar_artigo_por_id():
    """
    Testa se ao fazer uma requisição get para o endpoint /articles/{id_artigo} é retornado código 200
    """
    resp = client.get('/articles/1')
    assert resp.status_code == 200
