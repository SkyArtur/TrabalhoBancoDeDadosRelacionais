from fastapi import APIRouter, status, HTTPException
from schemas import Livro, LivroEstoque, Estoque


livros_router = APIRouter()


@livros_router.post('/livros', summary='Registra Livro', status_code=status.HTTP_201_CREATED)
async def post_livros(schema: LivroEstoque):
    try:
        return schema.save()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))


@livros_router.get('/livros')
async def get_livros():
    try:
        return Livro.get_livros()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))
