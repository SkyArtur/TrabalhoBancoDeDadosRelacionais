from pydantic import BaseModel


class Base(BaseModel):

    def tuple(self):
        return tuple(item for item in self.__dict__.values() if item is not None)
