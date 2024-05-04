from fastapi import APIRouter, status, HTTPException
from schemas import Livro


livros_router = APIRouter()


@livros_router.post('/', summary='Registra Livro', status_code=status.HTTP_201_CREATED)
async def post_livros(schema: Livro):
    try:
        return schema.save()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))


@livros_router.get('/')
async def get_livros():
    try:
        return Livro.get_livros()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))
