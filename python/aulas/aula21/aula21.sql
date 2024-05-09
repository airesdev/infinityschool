CREATE DATABASE IF NOT EXISTS escola;
USE escola;
DROP TABLE IF EXISTS alunos;
CREATE TABLE alunos (
	matricula INT PRIMARY KEY AUTO_INCREMENT, 
    nome VARCHAR(100) NOT NULL,
    idade INT,
    nota FLOAT
);

INSERT INTO alunos (nome, idade, nota) VALUES
('Leticia Freitas', 18, 9.7),
('Jonas Lopes', 18, 8.5);

select * from alunos