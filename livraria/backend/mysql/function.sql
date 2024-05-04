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

-- ##################################################################################################################
--  CLIENTES

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

-- ##################################################################################################################
-- EDITORAS

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

-- ##################################################################################################################
-- LIVROS

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

-- ##################################################################################################################
-- PEDIDOS

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

