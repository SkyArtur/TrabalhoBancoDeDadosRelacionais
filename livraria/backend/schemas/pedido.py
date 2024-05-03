from .base import Base
from typing import Type, Optional, List


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
