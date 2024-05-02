from abc import abstractmethod

import mysql
from pydantic import BaseModel
from config import session


class Base(BaseModel):

    def __repr__(self):
        return f'<{self.__class__.__name__}>: {self.__str__()}'

    @property
    def tuple(self):
        return tuple(value for value in self.__dict__.values() if value is not None)

    @classmethod
    def __search(cls, **kwargs):
        try:
            clientes = []
            query = kwargs.get('query')
            if not kwargs.get('_id'):
                for cliente in session.execute(query):
                    clientes.append(cls(**cliente))
                return clientes
            return cls(**session.execute(query, (kwargs.get('_id'),), fetchone=True))
        except (ConnectionError, AttributeError, ValueError, TypeError):
            return False

    def fetch(self, **kwargs):
        response = self.__search(**kwargs)
        if not response:
            return False
        return response

    @abstractmethod
    def fetchall(self, *args, **kwargs):
        ...

    @abstractmethod
    def fetchone(self, *args, **kwargs):
        ...

    @abstractmethod
    def insert(self, *args, **kwargs):
        ...

    @abstractmethod
    def update(self, *args, **kwargs):
        ...

    @abstractmethod
    def delete(self, *args, **kwargs):
        ...
