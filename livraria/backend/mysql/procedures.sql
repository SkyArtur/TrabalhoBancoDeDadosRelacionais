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
        select l.id, l.editora_id, d.nome as editora, l.titulo, l.autor, l.ano, l.isbn, l.preco, e.quantidade
        from livros l
        join estoque e on l.id = e.livro_id
        join editoras d on l.editora_id = d.id;
    end;


create procedure buscar_livro(_id int)
    begin
        select l.id, l.editora_id, d.nome as editora, l.titulo, l.autor, l.ano, l.isbn, l.preco, e.quantidade
        from livros l
        join estoque e on l.id = e.livro_id
        join editoras d on l.editora_id = d.id
        where l.id = _id;
    end;
