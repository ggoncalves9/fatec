
# Resumo com Explicação dos Comandos MySQL

## TP01 - MySQL

### Comandos e Utilização
- **`CREATE TABLE`:** Usado para criar a tabela `tb_vendas` com colunas para curso, aluno, estado e valor.
- **`INSERT INTO`:** Insere dados na tabela. Exemplo: Nome do curso, aluno, estado e valor de cada venda.
- **Consultas SQL:**
  1. **`SELECT *`:** Seleciona todas as colunas e linhas da tabela.
  2. **`SELECT coluna1, coluna2`:** Seleciona colunas específicas da tabela.
  3. **`ORDER BY`:** Ordena os resultados de uma consulta, crescente (ASC) ou decrescente (DESC).
  4. **`WHERE`:** Aplica filtros nos dados, como valor igual a 50 ou cursos específicos.

---

## TP02 - MySQL

### Comandos e Utilização
- **`CREATE TABLE`:** Usado para criar as tabelas `tb_produto` e `tb_venda`.
- **`INSERT INTO`:** Insere dados nas tabelas, como código, descrição do produto e valor total de venda.
- **Consultas SQL:**
  1. **`SUM`:** Soma o total de vendas realizadas.
  2. **`MIN` e `MAX`:** Identifica menor e maior valor de vendas.
  3. **`LIKE`:** Pesquisa por padrões, como nomes de produtos que contenham "Magazine".
  4. **`ORDER BY`:** Ordena produtos alfabeticamente ou valores em ordem decrescente.

---

## TP03 - MySQL

### Comandos e Utilização
- **`CREATE TABLE`:** Criação de tabelas `tb_clientes`, `tb_produtos`, e `tb_pedidos`.
- **`INSERT INTO`:** Insere dados detalhados, como informações de clientes, produtos e pedidos.
- **Consultas SQL:**
  1. **`GROUP BY`:** Agrupa os resultados por uma coluna, como clientes por sexo ou produtos por categoria.
  2. **`AVG`:** Calcula a média de valores, como custo médio dos produtos.
  3. **`SUM`:** Soma valores, como total de receita.
  4. **`JOIN`:** Relaciona tabelas para consultas mais complexas, como clientes e pedidos.

---

## TP04 - MySQL

### Comandos e Utilização
- **`CREATE TABLE`:** Criação de tabelas para clientes, produtos e vendas.
- **`INSERT INTO`:** Insere dados como nome do cliente, cidade, produtos e vendas.
- **Consultas SQL:**
  1. **`INNER JOIN`:** Junta tabelas exibindo apenas os registros correspondentes. Exemplo: Vendas e produtos.
  2. **`LEFT JOIN`:** Junta tabelas incluindo todos os registros da tabela à esquerda, mesmo sem correspondência.
  3. **`GROUP BY`:** Agrupa vendas por cliente ou cidade para obter contagens ou somas.
  4. **Subconsultas (`SUBQUERY`):** Permite consultas aninhadas, como listar produtos acima da média de preço.

---

## Explicações Gerais

### Comandos Comuns
1. **`CREATE TABLE`:** Define a estrutura de uma tabela com colunas e seus tipos de dados.
2. **`INSERT INTO`:** Adiciona dados às tabelas com valores específicos.
3. **`SELECT`:** Recupera dados de tabelas, com opções para filtros, ordenação e agrupamentos.
4. **`WHERE`:** Filtra linhas com base em condições específicas.
5. **`ORDER BY`:** Ordena os resultados em ordem crescente (padrão) ou decrescente.
6. **`GROUP BY`:** Agrupa linhas com valores semelhantes em colunas especificadas.

### Aplicações Práticas
- **Filtrar dados relevantes:** Usar `WHERE` e `LIKE` para encontrar registros específicos.
- **Análises:** `SUM`, `AVG`, `MIN`, `MAX` ajudam a calcular estatísticas.
- **Relação entre tabelas:** Usar `JOIN` para criar consultas mais ricas com múltiplas tabelas.
- **Estruturação de banco de dados:** `CREATE TABLE` e `INSERT INTO` organizam dados de forma eficiente.

