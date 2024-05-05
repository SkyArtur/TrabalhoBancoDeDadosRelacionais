from .base import Base
from typing import Type, Optional, List
from config import session


class Cliente(Base):
    id: Optional[int] = None
    nome: str
    telefone: str
    email: str
    endereco: str

    def save(self) -> 'Cliente':
        query = 'select inserir_cliente(%s, %s, %s, %s);'
        cliente = session.execute(query, self.tuple(), fetchone=True, commit=True)
        query = 'select * from clientes c where c.id = %s;'
        return Cliente(**session.execute(query, tuple(cliente.values()), fetchone=True))

    def update(self) -> 'Cliente':
        query = 'select atualizar_cliente(%s, %s, %s, %s, %s);'
        cliente = session.execute(query, self.tuple(), fetchone=True, commit=True)
        query = 'select * from clientes c where c.id = %s;'
        return Cliente(**session.execute(query, tuple(cliente.values()), fetchone=True))

    @classmethod
    def get_clientes(cls) -> List['Cliente']:
        clientes = []
        for cliente in session.execute('select * from clientes;'):
            clientes.append(cls(**cliente))
        return clientes
