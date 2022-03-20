"""Configurção para criar e utilizar um banco de dados com SQLAlchemy"""

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Busca a variavel de ambiente DATABASE_URL, caso não seja localizada nenhuma variavel de ambiente, irá ser utilizado
# a url default sqlite:///./flight_news.db
db_url = config('DATABASE_URL', default='sqlite:///./flight_news.db')


# Deixa db_url compativel com SQLAlchemy, pois a lib removeu o suporte para o endereço 'postgres://'
# atualmente só aceita postgresql://
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)


# Restante do código foi escrito conforme a documentação do FastAPI
# https://fastapi.tiangolo.com/tutorial/sql-databases/
SQLALCHEMY_DATABASE_URL = db_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def criar_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
