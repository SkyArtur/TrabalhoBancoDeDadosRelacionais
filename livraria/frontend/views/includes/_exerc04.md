# Lista de editoras e seus respectivos títulos
---
#### MySQL Query
---
```sql
select e.nome as editora, l.titulo
    from editoras e
    join livros l on e.id = l.editora_id
    order by e.nome desc;
```
---