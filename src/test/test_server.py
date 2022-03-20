import pytest


@pytest.fixture
def resp():
    """
    Fixture que retorna resposta de uma requisição get no endpoint raiz da API
    """
    return client.get('/')


def test_server(resp):
    """
    Testa se ao fazer uma requisição para o endpoint raiz é retornada status code 200 e a mensagem
    Back-end Challenge 2021 🏅 - Space Flight News
    """
    assert resp.status_code == 200
    assert resp.json == {'mensagem': 'Back-end Challenge 2021 🏅 - Space Flight News'}
