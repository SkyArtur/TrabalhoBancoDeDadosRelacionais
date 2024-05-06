-- Especialidades
insert into especialidades (especialidade) values ('cardiologia'), ('pediatria'), ('ginecologia');

-- Convênios
insert into convenios (empresa, tipo, vencimento, co_participacao) values
    ('Amicamed', 'individual', '2028-03-12', 15),
    ('Julimed', 'familiar', '2026-05-14', 12.5),
    ('SegVida', 'coletivo', '2025-05-12', 25),
    ('Nada Saude', 'empresarial', '2025-06-22', 32);


-- Consultas Particulares
insert into consulta_particular (paciente_id, medico_id, data, hora) values
    (1, 2, '2024-05-12', '10:50:00'),
    (2, 3, '2024-05-10', '15:25:00'),
    (4, 2, '2024-05-08', '08:10:00'),
    (5, 4, '2024-05-08', '09:50:00'),
    (4, 2, '2024-05-01', '10:30:00'),
    (1, 2, '2024-08-01', '10:50:00'),
    (2, 3, '2024-05-10', '16:25:00'),
    (1, 2, '2024-06-08', '11:10:00'),
    (3, 5, '2024-05-08', '09:15:00'),
    (4, 2, '2024-05-07', '10:30:00');

-- Consultas Convênios
insert into consulta_convenio (paciente_id, medico_id, convenio_id, data, hora) values
    (1, 2, 1, '2024-05-01', '10:50:00'),
    (1, 3, 2, '2024-06-10', '15:25:00'),
    (4, 2, 4, '2024-05-08', '08:10:00'),
    (2, 1, 1, '2024-05-08', '09:50:00'),
    (3, 2, 4, '2024-05-02', '10:25:00');

-- Estados
insert into estados (nome, uf) values ('paraná', 'PR');

-- Cidades
insert into cidades (nome, estado_id) values ('ponta grossa', 1), ('curitiba', 1);

select * from medicos;

select * from only pacientes;

select * from convenios;

select * from enderecos;

select * from pacientes;

select * from estados;

select * from especialidades;

select p.id, p.nome, p.sobrenome, c.empresa, c.tipo, c.vencimento, c.co_participacao from convenio_paciente
    join pacientes p on p.id = convenio_paciente.paciente_id
    join convenios c on c.id = convenio_paciente.convenio_id;

select p.nome as paciente, m.nome as "médico", data, hora from consulta_particular c
    join pacientes p on p.id =  c.paciente_id
    join medicos m on c.medico_id = m.id where m.id = 2;

select count(p.id) consultas, v.empresa  from consulta_convenio c
    join pacientes p on p.id =  c.paciente_id
    join convenios v on c.convenio_id = v.id
    group by v.empresa ;

select m.*, e.especialidade from medicos m join especialidades e on e.id = m.especialidade_id;


