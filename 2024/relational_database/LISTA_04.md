
parte 1)

INSERT INTO db_empresa02.tb_vendas (cd_venda, nm_curso, nm_aluno, Estado, Valor) VALUES
(1, 'Python', 'João', 'SP', 100.00),
(2, 'Html e CSS', 'Lucas', 'RJ', 50.00),
(3, 'Python', 'Alice', 'SP', 100.00),
(4, 'Html e CSS', 'Pedro', 'PE', 50.00),
(5, 'Html e CSS', 'Amanda', 'BA', 50.00),
(6, 'Power BI', 'Rita', 'RS', 80.00),
(7, 'Python', 'Julia', 'RJ', 100.00),
(8, 'Power BI', 'Caio', 'SP', 80.00),
(9, 'Power BI', 'Lara', 'MG', 80.00),
(10, 'Python', 'Rogério', 'AC', 100.00),
(11, 'SQL', 'Ana', 'PR', 90.00),
(12, 'SQL', 'Ricardo', 'RS', 90.00),
(13, 'SQL', 'Erica', 'SC', 90.00),
(14, 'Python', 'Carlos', 'SP', 100.00),
(15, 'SQL', 'Julio', 'MG', 90.00);


1)
SELECT * from tb_vendas;

2)
SELECT nm_curso,nm_aluno, estado, valor from tb_vendas;

3) 
SELECT * from tb_vendas
Limit 5;

4)
SELECT nm_curso AS 'Nome do Curso' ,nm_aluno AS 'Nome do Aluno', valor AS 'Preço Unitário' from tb_vendas;
 

5)
SELECT nm_aluno FROM tb_vendas ORDER BY nm_aluno;


6)
SELECT valor FROM tb_vendas ORDER BY valor DESC;

7)
SELECT valor FROM tb_vendas WHERE valor 
 IN (50,00);

8)
SELECT * FROM tb_vendas WHERE nm_curso = 'Python';

9)
SELECT * FROM tb_vendas ORDER BY nm_curso;

10)
SELECT * FROM tb_vendas ORDER BY estado;

