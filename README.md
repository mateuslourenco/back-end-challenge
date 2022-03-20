# Back-end Challenge 🏅 2021 - Space Flight News
>  This is a challenge by [Coodesh](https://lab.coodesh.com/public-challenges/back-end-challenge-2021)


### Back-end Challenge 🏅 2021 - Space Flight News é uma REST API desenvolvida em FastAPI baseada na API [Space Flight News](https://api.spaceflightnewsapi.net/v3/documentation)

# Projeto disponivel em
> [Space Flight News API](https://back-end-challenge-mateus.herokuapp.com/)

> [Documentação OpenAPI](https://back-end-challenge-mateus.herokuapp.com/docs#/)

# Tecnologias utilizadas
* Python
* Pipenv
* FastAPI
* Pytest
* Flake8
* GitHub Actions
* Heroku
* SQLAlchemy


# Como instalar e utilizar o projeto
1. Clone este repositorio e entre no diretorio
```
https://github.com/mateuslourenco/back-end-challenge.git
cd back-end-challenge
```
3. Instale o gerenciador de dependencias pipenv
```
pip install pipenv
```
4. Sincronize as dependencias com o pipenv sync
```
pipenv sync
```
5. Inicialize a API com o uvicorn
```
uvicorn src.server:app --reload --reload-dir=src
```


