from .base import Base
from typing import Type, Optional, List
from config import session


class Editora(Base):
    id: Optional[int | None] = None
    nome: str
    telefone: str
    email: str
    endereco: str

    def save(self):
        query = 'select inserir_editora(%s, %s, %s, %s);'
        editora = session.execute(query, self.tuple(), fetchone=True, commit=True)
        query = 'select * from editoras e where e.id = %s;'
        return Editora(**session.execute(query, tuple(editora.values()), fetchone=True))

    @classmethod
    def get_editoras(cls):
        editoras = []
        for editora in session.execute('select * from editoras;'):
            editoras.append(cls(**editora))
        return editoras
    e