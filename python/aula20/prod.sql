CREATE TABLE produtos (
	cod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    preco FLOAT,
    categoria VARCHAR(100)
);

INSERT INTO produtos VALUES
(DEFAULT, 'Mouse', 235, 'Periféricos'),
(DEFAULT, 'Teclado', '210', 'Periféricos'),
(DEFAULT, 'Fone', '130', 'Acessórios'),
(DEFAULT, 'Monitor', '899', 'Monitores');

# Atualizar um registro
UPDATE produtos SET preco = 130
WHERE cod = 1;

# Atualizando todos os registros (Periféricos)
USE aula20;
UPDATE produtos SET preco = preco * 0.9
WHERE categoria = 'Periféricos';

# Excluindo registros
DELETE FROM produtos WHERE cod = 1;

# Selecionando especificamente
SELECT nome, preco FROM produtos;

# Renomeando (Apenas na apresentação)
SELECT nome AS Nome, preco AS Preço FROM produtos;

# Contando a qtd de regoistros
SELECT count(*) FROM produtos;

# Obter maior preço
SELECT max(preco) FROM produtos;

# Obter menor preço
SELECT min(preco) FROM produtos;

# Obter soma dos preço
SELECT sum(preco) FROM produtos WHERE categoria = 'Periféricos';

# Realoizando Filtragens
SELECT * FROM produtos WHERE preco >= 140;

# OPERADOR LIKE (%)
# Buscando produtos que inicie com a letra T
SELECT * FROM produtos WHERE nome LIKE 'T%';