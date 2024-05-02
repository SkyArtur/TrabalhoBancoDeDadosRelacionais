from fastapi import APIRouter
from deps.msg import MSG
from schemas import Pedido

details = MSG(Pedido)

pedidos_router = APIRouter()


@pedidos_router.get('/', **MSG.docs('Pedidos').get('get'))
async def clientes():
    response = Pedido()
    return response.fetchall()


@pedidos_router.post('/', **MSG.docs('Pedidos').get('post'))
async def clientes(schema: Pedido):
    response = schema.insert()
    return response
