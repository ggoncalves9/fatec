
# Revisão de SQL - Introdução

## 1. **Comandos básicos do SQL**
Os comandos de SQL são geralmente divididos em quatro categorias principais:

### a) **DDL (Data Definition Language)**: Gerencia a estrutura do banco de dados.
- **CREATE**: Cria tabelas, bancos de dados, ou outros objetos.
  ```sql
  CREATE TABLE alunos (
      id INT PRIMARY KEY,
      nome VARCHAR(100),
      idade INT
  );
  ```
- **ALTER**: Modifica a estrutura de uma tabela.
  ```sql
  ALTER TABLE alunos ADD email VARCHAR(100);
  ```
- **DROP**: Remove tabelas ou bancos de dados.
  ```sql
  DROP TABLE alunos;
  ```

### b) **DML (Data Manipulation Language)**: Manipula os dados dentro das tabelas.
- **INSERT**: Insere dados em uma tabela.
  ```sql
  INSERT INTO alunos (id, nome, idade) VALUES (1, 'João', 20);
  ```
- **UPDATE**: Atualiza dados em uma tabela.
  ```sql
  UPDATE alunos SET idade = 21 WHERE id = 1;
  ```
- **DELETE**: Remove dados de uma tabela.
  ```sql
  DELETE FROM alunos WHERE id = 1;
  ```

### c) **DQL (Data Query Language)**: Consulta dados.
- **SELECT**: Consulta dados nas tabelas.
  ```sql
  SELECT * FROM alunos;
  SELECT nome, idade FROM alunos WHERE idade > 18;
  ```

### d) **DCL (Data Control Language)**: Controla permissões.
- **GRANT**: Concede permissões.
  ```sql
  GRANT SELECT ON alunos TO usuario;
  ```
- **REVOKE**: Remove permissões.
  ```sql
  REVOKE SELECT ON alunos FROM usuario;
  ```

---

## 2. **Filtros e Condições**
- **WHERE**: Filtra os resultados com base em uma condição.
  ```sql
  SELECT * FROM alunos WHERE idade >= 18;
  ```
- **AND, OR, NOT**: Combina condições.
  ```sql
  SELECT * FROM alunos WHERE idade > 18 AND nome LIKE 'J%';
  ```
- **BETWEEN**: Verifica se um valor está dentro de um intervalo.
  ```sql
  SELECT * FROM alunos WHERE idade BETWEEN 18 AND 25;
  ```
- **IN**: Verifica se um valor está em uma lista.
  ```sql
  SELECT * FROM alunos WHERE nome IN ('João', 'Maria');
  ```
- **LIKE**: Busca padrões (usado com `%` ou `_`).
  ```sql
  SELECT * FROM alunos WHERE nome LIKE 'M%'; -- Começa com 'M'
  ```

---

## 3. **Funções de Agregação**
- **COUNT**: Conta registros.
  ```sql
  SELECT COUNT(*) FROM alunos;
  ```
- **SUM**: Soma valores.
  ```sql
  SELECT SUM(idade) FROM alunos;
  ```
- **AVG**: Calcula a média.
  ```sql
  SELECT AVG(idade) FROM alunos;
  ```
- **MAX / MIN**: Obtém o maior/menor valor.
  ```sql
  SELECT MAX(idade), MIN(idade) FROM alunos;
  ```

---

## 4. **Ordenação e Agrupamento**
- **ORDER BY**: Ordena os resultados.
  ```sql
  SELECT * FROM alunos ORDER BY idade DESC;
  ```
- **GROUP BY**: Agrupa resultados.
  ```sql
  SELECT idade, COUNT(*) FROM alunos GROUP BY idade;
  ```
- **HAVING**: Filtra grupos (usado com `GROUP BY`).
  ```sql
  SELECT idade, COUNT(*) FROM alunos GROUP BY idade HAVING COUNT(*) > 1;
  ```

---

## 5. **Joins**
Os joins combinam dados de duas ou mais tabelas:
- **INNER JOIN**: Combina registros que existem nas duas tabelas.
  ```sql
  SELECT alunos.nome, cursos.nome 
  FROM alunos 
  INNER JOIN cursos ON alunos.curso_id = cursos.id;
  ```
- **LEFT JOIN**: Inclui todos os registros da tabela da esquerda.
  ```sql
  SELECT alunos.nome, cursos.nome 
  FROM alunos 
  LEFT JOIN cursos ON alunos.curso_id = cursos.id;
  ```
- **RIGHT JOIN**: Inclui todos os registros da tabela da direita.
- **FULL JOIN**: Combina todos os registros, com ou sem correspondência.

---

## 6. **Subconsultas**
- Subconsultas retornam resultados para serem usados em outras consultas.
  ```sql
  SELECT nome FROM alunos WHERE id IN (
      SELECT aluno_id FROM matriculas WHERE curso_id = 1
  );
  ```

---

## 7. **Outros Conceitos Importantes**
- **Alias**: Dá nomes temporários para tabelas ou colunas.
  ```sql
  SELECT nome AS aluno, idade AS anos FROM alunos;
  ```
- **LIMIT**: Limita o número de resultados.
  ```sql
  SELECT * FROM alunos LIMIT 5;
  ```
