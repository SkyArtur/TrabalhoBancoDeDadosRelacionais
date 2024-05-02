from .base import BaseModel, Base
from typing import Type, Optional, List
from config import session


class Cliente(Base):
    id: Optional[int | None] = None
    nome: Optional[str | None] = None
    telefone: Optional[str | None] = None
    email: Optional[str | None] = None
    endereco: Optional[str | None] = None

    def fetchone(self, *args, **kwargs) -> Type['Cliente'] | bool:
        return self.fetch(_id=self.id, query='call buscar_cliente_id(%s);')

    def fetchall(self, *args, **kwargs) -> List['Cliente'] | bool:
        return self.fetch(query='call buscar_clientes();')

    def insert(self, *args, **kwargs) -> Type['Cliente'] | bool:
        query_insert = 'select inserir_cliente(%s, %s, %s, %s);'
        cliente = session.execute(sql=query_insert, data=self.tuple, fetchone=True, commit=True)
        self.id = int(*cliente.values())
        if not self.id:
            return False
        return self.fetchone()

    def update(self, *args, **kwargs):
        try:
            query_update = 'select atualizar_cliente(%s, %s, %s, %s, %s);'
            cliente = self.fetchone()
            if cliente is None or not cliente:
                return False
            cliente.nome = cliente.nome if self.nome is None else self.nome
            cliente.telefone = cliente.telefone if self.telefone is None else self.telefone
            cliente.email = cliente.email if self.email is None else self.email
            cliente.endereco = cliente.endereco if self.endereco is None else self.endereco
            session.execute(query_update, cliente.tuple, fetchone=True, commit=True)
            return self.fetchone()
        except (TypeError, AttributeError, ValueError):
            return False

    def delete(self, *args, **kwargs):
        try:
            query_delete = 'select remover_cliente(%s);'
            cliente = self.fetchone()
            if cliente:
                session.execute(query_delete, (cliente.id,), fetchone=True, commit=True)
            return {
                'deleted': True,
                'cliente': cliente
            }
        except (TypeError, AttributeError, ValueError):
            return False
