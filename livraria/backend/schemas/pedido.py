from .base import BaseModel, Base
from typing import Type, Optional, List
from config import session


class Pedido(Base):
    cliente: Optional[int | str | None] = None
    livro: Optional[int | str | None] = None
    data: Optional[str | None] = None
    quantidade: Optional[int | None] = None

    def fetchone(self, *args, **kwargs) -> Type['Pedido'] | bool:
        ...

    def fetchall(self, *args, **kwargs) -> List['Pedido'] | bool:
        return self.fetch(query='call buscar_pedidos();')

    def insert(self, *args, **kwargs):
        query_insert = 'select inserir_pedido(%s, %s, %s, %s);'
        cliente = session.execute(sql=query_insert, data=self.tuple, fetchone=True, commit=True)
        print(cliente)

    def update(self, *args, **kwargs):
        ...

    def delete(self, *args, **kwargs):
        ...
