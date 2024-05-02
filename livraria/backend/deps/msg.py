from fastapi import status


class MSG:

    def __init__(self, model):
        self.model = model

    def get(self, local=None, _id=None):
        return {
            "get": f'{self.model} HTTP :: 500 :: Verifique conexão com o servidor.',
            "get_one": f'{self.model} HTTP :: 404 :: ID:{_id} não encontrado em nossa base de dados.',
            "post": f'{self.model} HTTP :: 409 :: ID:{_id} já se encontram em nossa base de dados.',
            "put_delete": f'{self.model} HTTP :: 404 :: ID:{_id} não encontrado. Nenhuma alteração foi feita.',
        }.get(local)

    @staticmethod
    def docs(model) -> dict:
        return {
            'get': {
                "status_code": status.HTTP_200_OK,
                "summary": f'Buscar todas os(as) {model}s registrados(as).'
            },
            'get_one': {
                "status_code": status.HTTP_200_OK,
                "summary": f'Buscar um registro de {model}.'
            },
            'post': {
                "status_code": status.HTTP_201_CREATED,
                "summary": f'Criar um novo registro de {model}.'
            },
            'put': {
                "status_code": status.HTTP_200_OK,
                "summary": f'Atualizar um registro de {model}.'
            },
            'delete': {
                "status_code": status.HTTP_200_OK,
                "summary": f'Apagar um registro de {model}.'
            },
        }
