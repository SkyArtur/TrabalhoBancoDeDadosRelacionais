import os
from faker import Faker
from random import choice
from pre_populate.connector import Database
from dotenv import load_dotenv

load_dotenv()

db = Database(
    os.getenv('DATABASE'),
    os.getenv('USER'),
    os.getenv('PASSWORD'),
    os.getenv('HOST'),
    os.getenv('PORT'),
)


class Perfil:
    faker = Faker('pt_BR')

    def __init__(self):
        self.nome = self.faker.first_name()
        self.sobrenome = self.faker.last_name()
        self.telefone = self.faker.phone_number()
        self.email = self.faker.email()

    def get_tuple(self):
        return tuple(item for item in self.__dict__.values())


class Paciente(Perfil):
    def __init__(self):
        super().__init__()
        self.cpf = self.faker.cpf()
        self.logradouro = f"{self.faker.street_prefix()} {self.faker.street_name()}"
        self.numero = self.faker.building_number()
        self.complemento = ''
        self.cep = self.faker.postcode()
        self.bairro = self.faker.neighborhood()
        self.cidade = 1
        self.convenio = choice([None, 1, 2, 3, 4])


class Medico(Perfil):
    def __init__(self):
        super().__init__()
        self.crm = self.faker.ssn()
        self.especialidade = choice([1, 2, 3])
        self.logradouro = f"{self.faker.street_prefix()} {self.faker.street_name()}"
        self.numero = self.faker.building_number()
        self.complemento = ''
        self.cep = self.faker.postcode()
        self.bairro = self.faker.neighborhood()
        self.cidade = 1


def cadastrar_estado_cidade(query):
    db.execute("insert into estados (nome, uf) values ('paraná', 'PR');", commit=True)
    db.execute("insert into cidades (nome, estado_id) values ('curitiba', 1);", commit=True)


def cadastrar_pacientes(numero: int):
    query = '''
        select * from cadastrar_paciente(
        _nome := %s, 
        _sobrenome := %s, 
        _telefone := %s, 
        _email := %s, 
        _cpf := %s, 
        _logradouro := %s, 
        _numero := %s, 
        _complemento := %s, 
        _cep := %s, 
        _bairro := %s, 
        _cidade_id := %s, 
        _convenio := %s);
    '''
    for _ in range(numero):
        paciente = Paciente()
        db.execute(query, paciente.get_tuple(), commit=True)


def cadastrar_medicos(numero: int):
    query = '''
        select * from cadastrar_medico(
        _nome := %s, 
        _sobrenome := %s, 
        _telefone := %s, 
        _email := %s, 
        _crm := %s,
        _especialidade_id := %s, 
        _logradouro := %s, 
        _numero := %s, 
        _complemento := %s, 
        _cep := %s, 
        _bairro := %s, 
        _cidade_id := %s);
    '''
    for _ in range(numero):
        medico = Medico()
        db.execute(query, medico.get_tuple(), commit=True)


cadastrar_medicos(12)