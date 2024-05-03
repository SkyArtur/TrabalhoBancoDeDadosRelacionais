create procedure buscar_clientes()
    begin
        select * from clientes;
    end;

create procedure buscar_cliente_id(_id int)
    begin
        select * from clientes where id = _id;
    end;

create procedure buscar_editoras()
    begin
        select * from editoras;
    end;

create procedure buscar_editora_id(_id int)
    begin
        select * from editoras where id = _id;
    end;


create procedure buscar_livros()
    begin
        select l.id, l.editora_id as editora, l.titulo, l.autor, l.ano, l.isbn, l.preco, e.quantidade
        from livros l join estoque e on l.id = e.livro_id;
    end;

create procedure buscar_livro_id(_id int)
    begin
        select l.id, l.editora_id as editora, l.titulo, l.autor, l.ano, l.isbn, l.preco, e.quantidade
        from livros l join estoque e on l.id = e.livro_id
        where l.id = _id;
    end;

create procedure buscar_pedidos()
    begin
        select c.nome as cliente, l.titulo as livro, p.data, i.quantidade from item_pedido i
        join pedidos p on p.id = i.pedido_id
        join livros l on i.livro_id = l.id
        join clientes c on c.id = p.cliente_id;
    end;



