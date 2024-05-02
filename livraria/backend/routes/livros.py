from fastapi import APIRouter
from deps.msg import MSG
from schemas import Livro

details = MSG(Livro)

livros_router = APIRouter()


@livros_router.get('/', **MSG.docs('Pedidos').get('get'))
async def livros():
    response = Livro()
    return response.fetchall()


@livros_router.get('/{_id}', **MSG.docs('Pedidos').get('get_one'))
async def livros(_id: int):
    response: Livro = Livro()
    response.id = _id
    return response.fetchone()


@livros_router.post('/', **MSG.docs('Pedidos').get('post'))
async def livros(schema: Livro):
    response = schema.insert()
    return response


@livros_router.put('/{_id}', **MSG.docs('Pedidos').get('put'))
async def livros(_id: int, schema: Livro):
    schema.id = _id
    response = schema.update()
    return response


@livros_router.delete('/{_id}', **MSG.docs('Pedidos').get('delete'))
async def livros(_id: int):
    response = Livro()
    response.id = _id
    return response.delete()
