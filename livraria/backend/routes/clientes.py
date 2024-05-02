from fastapi import APIRouter
from deps.msg import MSG
from schemas import Cliente

details = MSG(Cliente)

clientes_router = APIRouter()


@clientes_router.get('/', **MSG.docs('Pedidos').get('get'))
async def clientes():
    cliente = Cliente()
    return cliente.fetchall()


@clientes_router.get('/{_id}', **MSG.docs('Pedidos').get('get_one'))
async def clientes(_id: int):
    cliente = Cliente()
    cliente.id = _id
    return cliente.fetchone()


@clientes_router.post('/', **MSG.docs('Pedidos').get('post'))
async def clientes(schema: Cliente):
    cliente = schema.insert()
    return cliente


@clientes_router.put('/{_id}', **MSG.docs('Pedidos').get('put'))
async def clientes(_id: int, schema: Cliente):
    schema.id = _id
    cliente = schema.update()
    return cliente


@clientes_router.delete('/{_id}', **MSG.docs('Pedidos').get('delete'))
async def clientes(_id: int):
    cliente = Cliente()
    cliente.id = _id
    return cliente.delete()
