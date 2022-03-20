from starlette.testclient import TestClient

from src.server import app

client = TestClient(app)


def test_status_code_get_articles():
    """
    Testa se ao fazer uma requisição GET para o endpoint /articles/ é retornado código 200
    """
    resp = client.get('/articles/')
    assert resp.status_code == 200


def test_buscar_artigo_por_id():
    """
    Testa se ao fazer uma requisição GET para o endpoint /articles/{id_artigo} é retornado código 200
    """
    resp = client.get('/articles/1')
    assert resp.status_code == 200


def test_adicionar_novo_artigo():
    """
    Testa se ao fazer uma requisição POST para o endpoint /articles/ é retornado código 200
    """
    resp = client.post('/articles/')
    assert resp.status_code == 200


def test_editar_artigo():
    """
    Testa se ao fazer uma requisição PUT para o endpoint /articles/{id_artigo} é retornado código 200
    """
    resp = client.put('/articles/1')
    assert resp.status_code == 200


def test_deletar_artigo():
    """
    Testa se ao fazer uma requisição DELETE para o endpoint /articles/{id_artigo} é retornado código 200
    """
    resp = client.delete('/articles/1')
    assert resp.status_code == 200
