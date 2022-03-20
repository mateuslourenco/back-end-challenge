from fastapi import APIRouter

from src.schemas import schemas

router = APIRouter()


@router.get('/articles/', response_model=schemas.News)
def listar_todos_os_artigos():
    """
    Lista todos os artigos da base de dados
    """
    return {
        "id": 14337,
        "title": "General Dynamics’ cloud contract with NGA moves forward after Leidos withdraws protest",
        "url": "https://spacenews.com/",
        "imageUrl": "https://spacenews.com/wp-content/uploads/2022/03/gdit-uds-contract-2.png",
        "newsSite": "SpaceNews",
        "summary": "General Dynamics won a 10-year",
        "publishedAt": "2022-03-19T17:04:23.000Z",
        "updatedAt": "2022-03-19T17:04:23.739Z",
        "featured": False,
        "launches": [],
        "events": []
    }


@router.get('/articles/{id_artigo}')
def listar_artigo_por_id():
    """
    Obter a informação somente de um artigo
    """
    return {'msg': 'rota para articles/{id_artigo} criada'}


@router.post('/articles/')
def adicionar_artigo():
    """
    Adicionar um novo artigo
    """
    return {'msg': 'rota post para articles/ criada'}


@router.put('/articles/{id_artigo}')
def atualizar_artigo():
    """
    Atualizar artigo
    """
    return {'msg': 'rota put para articles/{id_artigo} criada'}


@router.delete('/articles/{id_artigo}')
def deletar_artigo():
    """
    Deletar artigo
    """
    return {'msg': 'rota put para articles/{id_artigo} criada'}
