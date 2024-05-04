from fastapi import APIRouter, status, HTTPException
from schemas import Editora

editoras_router = APIRouter()


@editoras_router.post('/', summary='Registrar editora', status_code=status.HTTP_201_CREATED)
async def post_editoras(schema: Editora):
    try:
        return schema.save()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))


@editoras_router.get('/', summary='Listar editora', status_code=status.HTTP_200_OK)
async def get_editoras():
    try:
        return Editora.get_editoras()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))


@editoras_router.put('/', summary='Editar editora', status_code=status.HTTP_200_OK)
async def put_editoras(schema: Editora):
    try:
        return schema.update()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))
