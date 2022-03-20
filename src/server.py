from fastapi import FastAPI

from src.infra.sqlalchemy.config.database import criar_db
from src.routers import rotas_articles

criar_db()

app = FastAPI()


@app.get('/')
def home():
    """
    Rota raiz da API
    """
    return {'mensagem': 'Back-end Challenge 2021 🏅 - Space Flight News'}


# Adicionar a rota dos artigos
app.include_router(rotas_articles.router)
