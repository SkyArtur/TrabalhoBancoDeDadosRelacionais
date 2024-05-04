from .base import Base
from typing import Type, Optional, List
from config import session


class ItemPedido(Base):
    pedido_id: int
    livro_id: int
    quantidade: int
    valor: float


class Pedido(Base):
    id: Optional[int | None] = None
    cliente_id: int
    data: str
    valor: float


class InsertPedido(Base):
    cliente_id: int
    livro_id: int
    data: str
    quantidade: int

    def save(self):
        query = 'select inserir_pedido(%s, %s, %s, %s);'
        check = session.execute(query, self.tuple(), commit=True)
        if not check:
            return False
        return True


class BuscarPedido(Base):
    id: int
    nome: str
    titulo: str
    data: str
    quantidade: int
    valor: float

    @classmethod
    def get(cls):
        return [cls(**item) for item in session.execute('call buscar_pedido();')]
