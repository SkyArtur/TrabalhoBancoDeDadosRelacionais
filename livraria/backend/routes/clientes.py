from fastapi import APIRouter, status, HTTPException
from schemas import Cliente
from config import session

clientes_router = APIRouter()


@clientes_router.post('/', summary='Registrar cliente', status_code=status.HTTP_201_CREATED)
async def post_clientes(schema: Cliente):
    try:
        return schema.save()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))


@clientes_router.get('/', summary='Listar clientes', status_code=status.HTTP_200_OK)
async def get_clientes():
    try:
        return Cliente.get_clientes()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))


@clientes_router.put('/', summary='Editar cliente', status_code=status.HTTP_200_OK)
async def put_clientes(schema: Cliente):
    try:
        return schema.update()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))
