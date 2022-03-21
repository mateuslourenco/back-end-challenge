"""
Script que consulta a API original e salva os artigos no banco de dados
"""

import requests
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import criar_db, engine
from src.infra.sqlalchemy.repositorios.news import RepositorioNews

criar_db()

# Lógica para pegar o ultimo artigo e usar como limite de artigos
url_com_ultimo_artigo = f'https://api.spaceflightnewsapi.net/v3/articles?_limit={1}'
response = requests.get(url_com_ultimo_artigo)
id_ultimo_artigo = response.json()[0]['id']

# Request passando o id do ultimo artigo como limit, sendo assim, vai retornar todos os artigos desde o utlimo
url_com_todos_os_artigos = f'https://api.spaceflightnewsapi.net/v3/articles?_limit={id_ultimo_artigo}'
resp = requests.get(url_com_todos_os_artigos)

session = Session(engine)


def criar_news_api(news, session: Session):
    """
    Função que chama o repositorio para salvar os dados no banco.
    Necessario passar uma 'news' e a sessao com o banco
    """
    return RepositorioNews(session).criar_news(news)


for news in resp.json():

    # Verifica se existe launches_id, launches_provider, events_id e events_provider na resposta.
    # Caso não exista, campos irão ficar em branco
    try:
        news['launches_id'] = news['launches'][0]['id']
    except IndexError:
        news['launches_id'] = ''

    try:
        news['launches_provider'] = news['launches'][0]['provider']
    except IndexError:
        news['launches_provider'] = ''

    try:
        news['events_id'] = news['events'][0]['id']
    except IndexError:
        news['events_id'] = ''

    try:
        news['events_provider'] = news['events'][0]['provider']
    except IndexError:
        news['events_provider'] = ''

    # Tenta salvar dados no banco, caso ID já exista, para a execuçao do script
    try:
        criar_news_api(news, session)
    except IntegrityError:
        print('Banco atualizado')
        break
