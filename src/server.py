from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    """
    Rota raiz da API
    """
    return {'mensagem': 'Back-end Challenge 2021 🏅 - Space Flight News'}
