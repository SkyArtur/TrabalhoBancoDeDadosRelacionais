# Lista quantitativa de livros cadastrados
---
#### MySQL Query
---
```sql
select l.titulo , d.nome, e.quantidade 
    from livros l
    join editoras d on l.editora_id = d.id
    join estoque e on l.id = e.livro_id
    order by e.quantidade desc;
```
---