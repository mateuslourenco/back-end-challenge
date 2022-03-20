import pytest


@pytest.fixture
def resp():
    return client.get('/')


def test_server(resp):
    assert resp.status_code == 200
    assert resp.json == {'mensagem': 'Back-end Challenge 2021 🏅 - Space Flight News'}
