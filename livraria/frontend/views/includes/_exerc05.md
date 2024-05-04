# Lista de editoras e a média dos preços de seus títulos
---
#### MySQL Query
---
```sql
select e.nome, round(avg(l.preco), 2) as media
    from editoras e
     join livraria.livros l on e.id = l.editora_id
    group by e.nome
    order by media desc;
```
---