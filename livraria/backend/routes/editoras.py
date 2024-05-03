from fastapi import APIRouter, status, HTTPException
from schemas import Editora
from config import session


editoras_router = APIRouter()


@editoras_router.post('/editoras', summary='Registrar editora', status_code=status.HTTP_201_CREATED)
async def post_editoras(schema: Editora):
    try:
        return schema.save()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))


@editoras_router.get('/editoras', summary='Listar clientes', status_code=status.HTTP_200_OK)
async def get_editoras():
    try:
        return Editora.get_editoras()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))
