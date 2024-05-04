# Lista de Clientes e Quantidade de livros comprados
---
#### MySQL Query
---
```sql
select c.nome, sum(p.quantidade) compras
    from clientes c
    join pedidos e on c.id = e.cliente_id
    join item_pedido p on e.id = p.pedido_id
    group by c.nome
    order by c.nome;
```
---