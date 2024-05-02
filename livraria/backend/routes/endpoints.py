from fastapi import APIRouter
from .clientes import clientes_router
from .editoras import editoras_router
from .livros import livros_router
from .pedidos import pedidos_router

router = APIRouter()

router.include_router(clientes_router, prefix='/clientes', tags=['Clientes'])
router.include_router(editoras_router, prefix='/editoras', tags=['Editoras'])
router.include_router(livros_router, prefix='/livros', tags=['Livros'])
router.include_router(pedidos_router, prefix='/pedidos', tags=['Pedidos'])
