CREATE DATABASE aula20;
USE aula20;

CREATE TABLE alunos(
	matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL, 
    nota FLOAT,
    dn DATE # aaaa-mm-dd
);

# Comando alter

# Como adicionar colunas?
ALTER TABLE alunos ADD curso VARCHAR(75) DEFAULT 'Python';

# Como remover uma coluna?
ALTER TABLE alunos DROP COLUMN nota;

# Como renomear uma coluna?
ALTER TABLE alunos CHANGE dn data_nascimento DATE;

# Como modificar uma coluna?
ALTER TABLE alunos MODIFY nome VARCHAR(150) NOT NULL; 

DESCRIBE alunos;

# Inserindo dados na tabela
INSERT INTO alunos (nome, curso, data_nascimento) VALUES
('Mariana', 'JavaScript', '2000-05-21'),
('Roberta', 'Node js', '2004-06-23');

INSERT INTO alunos VALUES
(DEFAULT, 'Augusto', '2002-02-15', 'Python');

SELECT * FROM alunos;
