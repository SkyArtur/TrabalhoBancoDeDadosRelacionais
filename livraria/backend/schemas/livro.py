from .base import Base
from typing import Type, Optional, List
from config import session


class Livro(Base):
    id: Optional[int] = None
    editora_id: int
    editora: Optional[str] = None
    titulo: str
    autor: str
    ano: int
    isbn: str
    preco: float
    quantidade: Optional[int] = None

    @classmethod
    def get_livros(cls) -> List['Livro']:
        livros = []
        for livro in session.execute('call buscar_livros();'):
            livros.append(cls(**livro))
        return livros

    def save(self) -> 'Livro':
        query_livro = 'select inserir_livro(%s, %s, %s, %s, %s, %s, %s);'
        livro = session.execute(query_livro, self.tuple(), fetchone=True, commit=True)
        return Livro(**session.execute('call buscar_livro();', (int(*livro.values()),), fetchone=True))
