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
            order by compras desc;
    end;

create procedure total_de_livros_cadastrados()
    begin
        select sum(e.quantidade) "Quantidade de livros em estoque" from livros l
        join estoque e on l.id = e.livro_id
        order by e.quantidade desc;
    end;

select nome from clientes order by nome desc;