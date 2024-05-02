create table if not exists clientes(
    id int unsigned primary key auto_increment,
    nome varchar(50) unique not null,
    telefone varchar(20) not null,
    email varchar(50) unique not null,
    endereco varchar(100) not null
);

create table if not exists editoras(
    id int unsigned primary key auto_increment,
    nome varchar(50) unique not null,
    telefone varchar(20) not null,
    email varchar(50) unique not null,
    endereco varchar(100) not null
);

create table if not exists pedidos(
    id int unsigned primary key auto_increment,
    cliente_id int unsigned not null,
    foreign key (cliente_id) references clientes(id) on delete no action ,
    data varchar(16),
    valor numeric(5,2)
);


create table if not exists livros(
    id int unsigned primary key auto_increment,
    editora_id int unsigned not null,
    foreign key (editora_id) references editoras(id) on delete no action ,
    titulo varchar(100) not null,
    autor varchar(50) not null,
    ano INT,
    isbn varchar(20) not null,
    preco numeric(5, 2)
);

create table if not exists item_pedido(
    pedido_id int unsigned not null ,
    livro_id int unsigned not null ,
    foreign key (pedido_id) references pedidos(id) on delete no action,
    foreign key (livro_id) references livros(id) on delete no action,
    quantidade int,
    valor decimal(5, 2)
);

create table if not exists estoque(
    livro_id int unsigned not null ,
    foreign key (livro_id) references livros(id) on delete cascade,
    quantidade int
);

