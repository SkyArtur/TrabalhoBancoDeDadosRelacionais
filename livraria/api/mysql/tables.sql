create table if not exists clientes(
    id int unsigned primary key auto_increment,
    nome varchar(255) unique not null,
    telefone varchar(20) not null,
    email varchar(50) unique not null,
    endereco varchar(100) not null,
    password varchar(255) not null
);

create table if not exists editoras(
    id int unsigned primary key auto_increment,
    nome varchar(255) unique not null,
    telefone varchar(20) not null,
    email varchar(50) unique not null,
    endereco varchar(100) not null
);




