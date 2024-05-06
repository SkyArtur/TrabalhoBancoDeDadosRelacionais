


# Exercício proposto na disciplina: Banco de dados Relacionai

> *Bacharelado em Engrenharia de Software - Uninter*
> *Profº Ricardo Sonaglio Alba

## Proposta 1 - Clínica

### Modelo Entidade Relacionamento 

![MRE-01-Branco.png](assets%2FMRE-01-Branco.png)

### Tabelas
```sql
create table if not exists estados (
    id serial primary key,
    nome varchar(150) not null ,
    uf char(2) not null unique not null
);

create table if not exists cidades (
    id serial primary key,
    nome varchar(150) not null,
    estado_id int not null,
    foreign key (estado_id) references estados(id)
        on delete no action
);

create table if not exists enderecos (
    id serial primary key,
    logradouro varchar(255) not null ,
    numero varchar(8) ,
    complemento varchar(255) ,
    cep varchar(15) ,
    bairro varchar(120) not null ,
    cidade_id int not null ,
    foreign key (cidade_id) references cidades(id)
        on delete no action
);

create table if not exists especialidades(
    id serial primary key,
    especialidade varchar(50) not null
);

create table if not exists perfis(
    id serial primary key,
    nome varchar(100) not null,
    sobrenome varchar(100) not null,
    telefone varchar(30) not null,
    email varchar(150) not null unique,
    endereco_id int not null ,
    foreign key (endereco_id) references enderecos(id)
        on delete no action
);

create table if not exists pacientes(
    id serial primary key,
    cpf varchar(16) not null unique
) inherits (perfis);

create table if not exists medicos(
    id serial primary key,
    crm varchar(16) not null unique,
    especialidade_id int not null,
    foreign key (especialidade_id)
        references especialidades(id)
) inherits (perfis);

create table if not exists convenios(
    id serial primary key,
    empresa varchar(150) not null unique,
    tipo varchar(30) not null,
    vencimento date not null ,
    co_participacao numeric(4,2) not null
);

create table if not exists consulta_particular(
    paciente_id int not null ,
    foreign key (paciente_id) references pacientes(id) on delete  no action,
    medico_id int not null,
    foreign key (medico_id) references medicos(id) on delete  no action,
    data date not null ,
    hora time not null
);

create table if not exists consulta_convenio(
    paciente_id int not null ,
    foreign key (paciente_id) references pacientes(id) on delete  no action,
    medico_id int not null,
    foreign key (medico_id) references medicos(id) on delete  no action,
    convenio_id int not null,
    foreign key (convenio_id) references convenios(id) on delete  no action,
    data date not null ,
    hora time not null
);

create table if not exists convenio_paciente(
    convenio_id int not null,
    paciente_id int not null,
    foreign key (convenio_id) references convenios(id) on delete  no action,
    foreign key (paciente_id) references pacientes(id) on delete no action
);

```

### Funções
```sql
create or replace function cadastrar_paciente(
    _nome varchar, _sobrenome varchar, _telefone varchar, _email varchar, _cpf varchar,
    _logradouro varchar, _numero varchar, _complemento varchar, _cep varchar, _bairro varchar,
    _cidade_id int, _convenio int default null
) returns int as $$
        declare
            new_id int default 0;
        begin
            insert into enderecos (logradouro, numero, complemento, cep, bairro, cidade_id)
                values (_logradouro, _numero, _complemento, _cep, _bairro, _cidade_id) returning id into new_id;
            insert into pacientes (nome, sobrenome, telefone, email, cpf, endereco_id)
                values (_nome, _sobrenome, _telefone, _email, _cpf, new_id) returning id into new_id;
            if _convenio is not null
                then
                insert into convenio_paciente (convenio_id, paciente_id) values (_convenio, new_id);
            end if;
            return new_id;
        end;
    $$ language plpgsql;

create or replace function cadastrar_medico(
    _nome varchar, _sobrenome varchar, _telefone varchar, _email varchar, _crm varchar, _especialidade_id int,
    _logradouro varchar, _numero varchar, _complemento varchar, _cep varchar, _bairro varchar, _cidade_id int
) returns int as $$
        declare
            new_id int default 0;
        begin
            insert into enderecos (logradouro, numero, complemento, cep, bairro, cidade_id)
                values (_logradouro, _numero, _complemento, _cep, _bairro, _cidade_id) returning id into new_id;
            insert into medicos (nome, sobrenome, telefone, email, endereco_id, crm, especialidade_id)
                values (_nome, _sobrenome, _telefone, _email, new_id, _crm, _especialidade_id) returning id into new_id;
            return new_id;
        end;
    $$ language plpgsql;
```


