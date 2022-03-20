from fastapi import FastAPI

from src.routers import rotas_articles

app = FastAPI()


@app.get('/')
def home():
    """
    Rota raiz da API
    """
    return {'mensagem': 'Back-end Challenge 2021 🏅 - Space Flight News'}


# Adicionar a rota dos artigos
app.include_router(rotas_articles.router)
