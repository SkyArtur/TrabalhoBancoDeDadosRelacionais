from .base import Base
from config import session


class Exerc02(Base):
    titulo: str
    nome: str
    quantidade: int

    @classmethod
    def get(cls):
        return [cls(**exerc) for exerc in session.execute('call quantitativo_de_livros_cadastrados();')]


class Exerc03(Base):
    nome: str

    @classmethod
    def get(cls):
        return [cls(**exerc) for exerc in session.execute('select nome from clientes order by nome asc;')]


class Exerc04(Base):
    editora: str
    titulo: str

    @classmethod
    def get(cls):
        return [cls(**exerc) for exerc in session.execute('call listar_editora_e_titulos();')]


class Exerc05(Base):
    nome: str
    media: float

    @classmethod
    def get(cls):
        return [cls(**exerc) for exerc in session.execute('call editora_media_de_precos();')]


class Exerc06(Base):
    nome: str
    compras: int

    @classmethod
    def get(cls):
        return [cls(**exerc) for exerc in session.execute('call cliente_e_numero_de_compras();')]
