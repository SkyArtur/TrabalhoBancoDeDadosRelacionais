# Execício Prático - Livraria

> Prática proposta pela disciplina de banco de dados relacionais, do curso de bacharelado em engenharia de software 
do Centro Universitário Internacional - Uninter - ministrada pelo professor Ricardo Sonaglio Albano.

![MRE-livraria](https://github.com/SkyArtur/TrabalhoBancoDeDadosRelacionais/assets/93395366/f33b8132-5c8d-4d77-8132-3fb0641476f8)

### Tabelas

Foram desenvolvidas as tabelas conforme a modelagem apresentada. Respeitando a solicitação para a não nulidade de valores
 e as requeridas relações entre em entidades.

```mysql
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
    data varchar(16) not null ,
    valor numeric(5,2) not null
);


create table if not exists livros(
    id int unsigned primary key auto_increment,
    editora_id int unsigned not null,
    foreign key (editora_id) references editoras(id) on delete no action ,
    titulo varchar(100) not null,
    autor varchar(50) not null,
    ano int not null not null ,
    isbn varchar(20) not null,
    preco numeric(5, 2) not null
);

create table if not exists item_pedido(
    pedido_id int unsigned not null ,
    livro_id int unsigned not null ,
    foreign key (pedido_id) references pedidos(id) on delete no action,
    foreign key (livro_id) references livros(id) on delete no action,
    quantidade int not null ,
    valor decimal(5, 2) not null
);

create table if not exists estoque(
    livro_id int unsigned not null ,
    foreign key (livro_id) references livros(id) on delete cascade,
    quantidade int not null
);
```

### Funções

Para a realização de inserções e atualizações foram implementadas funções. 

```mysql
create function inserir_cliente(_nome varchar(50), _telefone varchar(20), _email varchar(50), _endereco varchar(100))
    returns integer deterministic
        begin
            declare existe boolean default false;
            declare cliente integer default null;
            select true into existe from clientes where email = _email;
            if (not existe)
               then
               insert into clientes (nome, telefone, email, endereco)
                   value (_nome, _telefone, _email, _endereco);
                    select last_insert_id() into cliente;
               return cliente;
            else
                return 0;
            end if;
        end;

create function atualizar_cliente(_id int, _nome varchar(50), _telefone varchar(20), _email varchar(50), _endereco varchar(100))
    returns integer deterministic
        begin
            declare existe boolean default false;
            select true into existe from clientes where id = _id;
            if (existe)
               then
               update clientes set nome = _nome, telefone = _telefone, email = _email, endereco = _endereco
                   where id = _id;
               return _id;
            else
                return 0;
            end if;
        end;

create function inserir_editora(_nome varchar(50), _telefone varchar(20), _email varchar(50), _endereco varchar(100))
    returns integer deterministic
        begin
            declare existe boolean default false;
            declare editora integer default null;
            select true into existe from editoras where email = _email;
            if (not existe)
               then
               insert into editoras (nome, telefone, email, endereco)
                   value (_nome, _telefone, _email, _endereco);
               select last_insert_id() into editora;
               return editora;
            else
                return 0;
            end if;
        end;

create function atualizar_editora(_id int, _nome varchar(50), _telefone varchar(20), _email varchar(50), _endereco varchar(100))
    returns integer deterministic
        begin
            declare existe boolean default false;
            select true into existe from editoras where id = _id;
            if (existe)
               then
               update editoras set nome = _nome, telefone = _telefone, email = _email, endereco = _endereco
                   where id = _id;
               return _id;
            else
                return 0;
            end if;
        end;

create function inserir_livro(_editora_id int, _titulo varchar(100), _autor varchar(50), _ano int, _isbn varchar(20), _preco numeric(5, 2), _quantidade int)
    returns integer deterministic
        begin
            declare existe boolean default false;
            declare livro int default null;
            select true into existe from editoras where id = _editora_id;
            if existe
                then
                insert into livros (editora_id, titulo, autor, ano, isbn, preco)
                    values (_editora_id, _titulo, _autor, _ano, _isbn, _preco);
                select last_insert_id() into livro;
                insert into estoque (livro_id, quantidade) values (livro, _quantidade);
                return livro;
            else
                return 0;
            end if;
        end;

create function inserir_pedido(_cliente_id int, _livro_id int, _data varchar(16), _quantidade int)
    returns boolean deterministic
        begin
            declare pedido int default null;
            declare total numeric;
            declare existe boolean default false;
            select true into existe from livros l
                join estoque e ON l.id = e.livro_id
                where l.id = _livro_id and e.quantidade >= _quantidade;
            if (existe)
                then
                select calcular_valor_item(_livro_id, _quantidade) into total;
                insert into pedidos (cliente_id, data, valor) values (_cliente_id, _data, total);
                select last_insert_id() into pedido;
                insert into item_pedido (pedido_id, livro_id, quantidade, valor)
                    values (pedido, _livro_id, _quantidade, total);
                return true;
            else
                return false;
            end if;
        end;
```

### Procedures

As consultas foram realizadas a partir da abordagem em procedures.

```mysql
create procedure buscar_livros()
    begin
        select l.id, l.editora_id, d.nome as editora, l.titulo, l.autor, l.ano, l.isbn, l.preco, e.quantidade
        from livros l
        join estoque e on l.id = e.livro_id
        join editoras d on l.editora_id = d.id;
    end;

create procedure buscar_livro(_id int)
    begin
        select l.id, l.editora_id, d.nome as editora, l.titulo, l.autor, l.ano, l.isbn, round(l.preco, 2), e.quantidade
        from livros l
        join estoque e on l.id = e.livro_id
        join editoras d on l.editora_id = d.id
        where l.id = _id;
    end;

create procedure buscar_pedido()
    begin
        select p.id, c.nome, l.titulo, p.data, pd.quantidade, pd.valor
            from item_pedido pd
            join pedidos p on pd.pedido_id = p.id
            join livros l on pd.livro_id = l.id
            join clientes c on p.cliente_id = c.id;
    end;

-- EXERCÍCIOS

create procedure quantitativo_de_livros_cadastrados()
    begin
        select l.titulo , d.nome, e.quantidade from livros l
        join editoras d on l.editora_id = d.id
        join estoque e on l.id = e.livro_id
        order by e.quantidade desc;
    end;

create procedure clientes_em_ordem_decrescente()
    begin
        select nome from clientes order by nome desc;
    end;

create procedure listar_editora_e_titulos()
    begin
        select e.nome as editora, l.titulo
            from editoras e
            join livros l on e.id = l.editora_id
            order by e.nome desc;
    end;

create procedure editora_media_de_precos()
    begin
        select e.nome, round(avg(l.preco), 2) as media
            from editoras e
            join livraria.livros l on e.id = l.editora_id
            group by e.nome
            order by media desc;
    end;

create procedure cliente_e_numero_de_compras()
    begin
        select c.nome, sum(p.quantidade) compras
            from clientes c
            join pedidos e on c.id = e.cliente_id
            join item_pedido p on e.id = p.pedido_id
            group by c.nome
            order by c.nome;
    end;
```

### Extras: 

Foram implementados dispositivos extras para a realização do cálculo do valor de uma venda po uma de função que recebe 
o id do livro comprado e quantidade. Também foi implementado um gatilho (trigger) para atualizar o estoque.

```mysql
create function calcular_valor_item(_livro_id int, quantidade int)
    returns numeric deterministic
        begin
            declare preco numeric;
            select l.preco into preco from livros l where id = _livro_id;
            return round(preco * quantidade, 2);
        end;

create trigger atualizar_estoque
    after insert on item_pedido
    for each row
    begin
        update estoque set quantidade = quantidade - new.quantidade
        where livro_id = NEW.livro_id;
    end;
```

### Aplicação

Para a realização dos cadastros necessários, bem como as consultas solicitadas para a atividade prática, foi desenvolvida 
um pequeno sistema que consiste de:
- uma aplicação frontend feita em NodeJS e utilizando o framework Express JS;

![APP-livraria.png](assets%2FAPP-livraria.png)

- uma interface de programação de aplicação (API) feita em Python utilizando o framework FastApi;

![API-livraria.png](assets%2FAPI-livraria.png)

Para comunicação com o banco de dados foi implementado um connector personalizado que utiliza a biblioteca mysql.connector.
É um objeto em padrão singleton muito simples, mas que bem ao seu propósito.
```python
import mysql.connector


class Connector:
    __instance: 'Connector' = None

    def __new__(cls, *args, **kwargs) -> 'Connector':
        if cls.__instance is None:
            cls.__instance = super(Connector, cls).__new__(cls)
        return cls.__instance

    def __init__(self, **kwargs) -> None:
        self.conn = None
        self.cur = None
        self.response = None

        self.params = kwargs.get('params')

    def __connect(self) -> mysql.connector.connection:
        return mysql.connector.connect(**self.params)

    def execute(self, sql: str, data: tuple = None, fetchone: bool = False, commit: bool = False):
        try:
            self.conn = self.__connect()
            self.cur = self.conn.cursor(dictionary=True)
            self.cur.execute(sql, data)
            response = self.cur.fetchone() if fetchone else self.cur.fetchall()
        except (mysql.connector.Error, AttributeError, TypeError) as err:
            print(err)
            # raise ConnectionError
        else:
            if commit:
                self.conn.commit()
            return response
        finally:
            try:
                self.cur.close()
                self.conn.close()
            except (mysql.connector.Error, AttributeError, TypeError) as err:
                print(err)
                # raise ConnectionError

```

### Docker

A aplicação pode ser executada a partir de containers docker, executando os comandos abaixo em um terminal iniciado na
pasta raiz do projeto (**./livraria**). 

- Criar o serviço:
```shell
docker-compose up -d
```
- Criar as entidades do banco de dados.
```shell
docker exec -it api_livraria python setup.py
```

A aplicação rodará na porta em: 
```shell
http://localhost:3000
```

Esta aplicação é meramente uma atividade didática e não tem finalidade real além do execício de habilidades em 
programação e de fazer parte de um repositório de códigos pessoais.

