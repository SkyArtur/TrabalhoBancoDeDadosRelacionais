from fastapi import APIRouter, status, HTTPException
from schemas import BuscarPedido, InsertPedido
from config import session

pedidos_router = APIRouter()


@pedidos_router.post('/', summary='Registrar pedido', status_code=status.HTTP_201_CREATED)
async def post_clientes(schema: InsertPedido):
    try:
        return schema.save()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))


@pedidos_router.get('/', summary='Listar pedidos', status_code=status.HTTP_200_OK)
async def get_pedidos():
    try:
        return BuscarPedido.get()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))