from .base import Base
from typing import Type, Optional, List
from config import session


class Livro(Base):
    id: Optional[int | None] = None
    editora_id: int
    titulo: str
    autor: str
    ano: int
    isbn: str
    preco: float

    @classmethod
    def get_livros(cls) -> List['Livro']:
        livros = []
        for livro in session.execute('select * from livros;'):
            livros.append(cls(**livro))
        return livros


class Estoque(Base):
    livro_id: int
    quantidade: int


class LivroEstoque(Base):
    editora_id: int
    titulo: str
    autor: str
    ano: int
    isbn: str
    preco: float
    quantidade: int

    def save(self) -> Livro:
        query_livro = 'select inserir_livro(%s, %s, %s, %s, %s, %s);'
        livro = Livro(
            editora_id=self.editora_id,
            titulo=self.titulo,
            autor=self.autor,
            ano=self.ano,
            isbn=self.isbn,
            preco=self.preco,
        )
        livro = session.execute(query_livro, livro.tuple(), fetchone=True, commit=True)
        livro_id = int(*livro.values())
        estoque = Estoque(
            livro_id=livro_id,
            quantidade=self.quantidade,
        )
        session.execute('select insert_estoque(%s, %s);', estoque.tuple(), commit=True)
        return Livro(**session.execute('select * from livros where id = %s;', (livro_id,), fetchone=True))
