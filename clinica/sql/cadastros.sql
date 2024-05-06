create or replace function cadastrar_paciente(
    _nome varchar, _sobrenome varchar, _telefone varchar, _email varchar, _cpf varchar,
    _logradouro varchar, _numero varchar, _complemento varchar, _cep varchar, _bairro varchar,
    _cidade_id int, _convenio int default null
) returns int as $$
        declare
            new_id int default 0;
        begin
            insert into enderecos (logradouro, numero, complemento, cep, bairro, cidade_id)
                values (_logradouro, _numero, _complemento, _cep, _bairro, _cidade_id) returning id into new_id;
            insert into pacientes (nome, sobrenome, telefone, email, cpf, endereco_id)
                values (_nome, _sobrenome, _telefone, _email, _cpf, new_id) returning id into new_id;
            if _convenio is not null
                then
                insert into convenio_paciente (convenio_id, paciente_id) values (_convenio, new_id);
            end if;
            return new_id;
        end;
    $$ language plpgsql;

create or replace function cadastrar_medico(
    _nome varchar, _sobrenome varchar, _telefone varchar, _email varchar, _crm varchar, _especialidade_id int,
    _logradouro varchar, _numero varchar, _complemento varchar, _cep varchar, _bairro varchar, _cidade_id int
) returns int as $$
        declare
            new_id int default 0;
        begin
            insert into enderecos (logradouro, numero, complemento, cep, bairro, cidade_id)
                values (_logradouro, _numero, _complemento, _cep, _bairro, _cidade_id) returning id into new_id;
            insert into medicos (nome, sobrenome, telefone, email, endereco_id, crm, especialidade_id)
                values (_nome, _sobrenome, _telefone, _email, new_id, _crm, _especialidade_id) returning id into new_id;
            return new_id;
        end;
    $$ language plpgsql;
