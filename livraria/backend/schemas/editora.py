from .base import BaseModel, Base
from typing import Type, Optional, List
from config import session


class Editora(Base):
    id: Optional[int | None] = None
    nome: Optional[str | None] = None
    telefone: Optional[str | None] = None
    email: Optional[str | None] = None
    endereco: Optional[str | None] = None

    def fetchone(self, *args, **kwargs) -> Type['Editora'] | bool:
        return self.fetch(_id=self.id, query='call buscar_editora_id(%s);')

    def fetchall(self, *args, **kwargs) -> List['Editora'] | bool:
        return self.fetch(query='call buscar_editoras();')

    def insert(self, *args, **kwargs) -> Type['Editora'] | bool:
        query_insert = 'select inserir_editora(%s, %s, %s, %s);'
        editora = session.execute(sql=query_insert, data=self.tuple, fetchone=True, commit=True)
        self.id = int(*editora.values())
        if not self.id:
            return False
        return self.fetchone()

    def update(self, *args, **kwargs):
        try:
            query_update = 'select atualizar_editora(%s, %s, %s, %s, %s);'
            editora = self.fetchone()
            if editora is None or not editora:
                return False
            editora.nome = editora.nome if self.nome is None else self.nome
            editora.telefone = editora.telefone if self.telefone is None else self.telefone
            editora.email = editora.email if self.email is None else self.email
            editora.endereco = editora.endereco if self.endereco is None else self.endereco
            session.execute(query_update, editora.tuple, fetchone=True, commit=True)
            return self.fetchone()
        except (TypeError, AttributeError, ValueError):
            return False

    def delete(self, *args, **kwargs):
        try:
            query_delete = 'select remover_editora(%s);'
            editora = self.fetchone()
            if editora:
                session.execute(query_delete, (editora.id,), fetchone=True, commit=True)
            return {
                'deleted': True,
                'cliente': editora
            }
        except (TypeError, AttributeError, ValueError):
            return False
