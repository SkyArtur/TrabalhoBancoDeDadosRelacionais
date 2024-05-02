from fastapi import APIRouter
from deps.msg import MSG
from schemas import Editora

details = MSG(Editora)

editoras_router = APIRouter()


@editoras_router.get('/', **MSG.docs('Pedidos').get('get'))
async def editora():
    response = Editora()
    return response.fetchall()


@editoras_router.get('/{_id}', **MSG.docs('Pedidos').get('get_one'))
async def editoras(_id: int):
    response: Editora = Editora()
    response.id = _id
    return response.fetchone()


@editoras_router.post('/', **MSG.docs('Pedidos').get('post'))
async def editoras(schema: Editora):
    response = schema.insert()
    return response


@editoras_router.put('/{_id}', **MSG.docs('Pedidos').get('put'))
async def editoras(_id: int, schema: Editora):
    schema.id = _id
    response = schema.update()
    return response


@editoras_router.delete('/{_id}', **MSG.docs('Pedidos').get('delete'))
async def editoras(_id: int):
    response = Editora()
    response.id = _id
    return response.delete()
