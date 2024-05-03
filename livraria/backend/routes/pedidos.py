from fastapi import APIRouter, status, HTTPException
from schemas import Pedido
from config import session

pedidos_router = APIRouter()


@pedidos_router.post('/pedidos', summary='Registrar pedido', status_code=status.HTTP_201_CREATED)
async def post_clientes(schema: Pedido):
    try:
        query = 'select inserir_pedido(%s, %s, %s, %s);'
        pedidos = session.execute(query, schema.tuple(), fetchone=True, commit=True)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL, detail=str(e))
    return pedidos
