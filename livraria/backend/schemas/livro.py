from .base import BaseModel, Base
from typing import Type, Optional, List
from config import session


class Livro(Base):
    id: Optional[int | None] = None
    editora: Optional[str | int | None] | None = None
    titulo: Optional[str | None] = None
    autor: Optional[str | None] = None
    ano: Optional[int | None] = None
    isbn: Optional[str | None] = None
    preco: Optional[float | None] = None
    quantidade: Optional[int | None] = None

    def fetchone(self, *args, **kwargs) -> Type['Livro'] | bool:
        return self.fetch(_id=self.id, query='call buscar_livro_id(%s);')

    def fetchall(self, *args, **kwargs) -> List['Livro'] | bool:
        return self.fetch(query='call buscar_livros();')

    def insert(self, *args, **kwargs) -> Type['Livro'] | bool:
        query_insert = 'select inserir_livro(%s, %s, %s, %s, %s, %s, %s);'
        livro = session.execute(sql=query_insert, data=self.tuple, fetchone=True, commit=True)
        self.id = int(*livro.values())
        if not self.id:
            return False
        return self.fetchone()

    def update(self, *args, **kwargs):
        try:
            query_update = 'select atualizar_livro(%s, %s, %s, %s, %s, %s, %s, %s);'
            livro = self.fetchone()
            if livro is None or not livro:
                return False
            livro.titulo = livro.titulo if self.titulo is None else self.titulo
            livro.autor = livro.autor if self.autor is None else self.autor
            livro.ano = livro.ano if self.ano is None else self.ano
            livro.isbn = livro.isbn if self.isbn is None else self.isbn
            livro.preco = livro.preco if self.preco is None else self.preco
            session.execute(query_update, livro.tuple, fetchone=True, commit=True)
            return self.fetchone()
        except (TypeError, AttributeError, ValueError):
            return False

    def delete(self, *args, **kwargs):
        try:
            query_delete = 'select remover_livro(%s);'
            editora = self.fetchone()
            if editora:
                session.execute(query_delete, (editora.id,), fetchone=True, commit=True)
            return {
                'deleted': True,
                'cliente': editora
            }
        except (TypeError, AttributeError, ValueError):
            return False
