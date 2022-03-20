from fastapi import APIRouter

router = APIRouter()


@router.get('/articles/')
def listar_todos_os_artigos():
    """
    Lista todos os artigos da base de dados
    """
    return {'msg': 'rota articles criada'}
