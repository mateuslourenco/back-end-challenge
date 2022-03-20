from fastapi import APIRouter

router = APIRouter()


@router.get('/articles/')
def listar_todos_os_artigos():
    """
    Lista todos os artigos da base de dados
    """
    return {'msg': 'rota articles criada'}


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
def atualizar_artigo():
    """
    Deletar artigo
    """
    return {'msg': 'rota put para articles/{id_artigo} criada'}
