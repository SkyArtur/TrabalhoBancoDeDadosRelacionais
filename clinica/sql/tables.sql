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




