# Outras Operações da Álgebra Relacional e seus Equivalentes em SQL

| Operação da Álgebra Relacional | Descrição | Equivalente em SQL |
|--------------------------------|-----------|---------------------|
| **União (∪)**                  | Combina duas relações e elimina duplicatas. | `UNION` |
| **Interssecção (∩)**           | Retorna as linhas (tuplas) que são comuns a duas tabelas (relações) |  
EXCEPT e INTERSECT |
| **Diferença (-)**              | Retorna tuplas que estão na primeira relação e não na segunda. | `EXCEPT` ou `MINUS` (dependendo do sistema de banco de dados) |
| **Produto Cartesiano (×)**     | Combina cada tupla da primeira relação com cada tupla da segunda. | `CROSS JOIN` |
| **Seleção (σ)**                | Filtra as tuplas de uma relação com base em uma condição. | `SELECT ... WHERE ...` |
| **Projeção (π)**               | Seleciona apenas algumas colunas de uma relação. | `SELECT ...` (especificando colunas) |
| **Junção (⨝)**                 | Combina tuplas de duas relações com base em uma condição de correspondência. | `JOIN` (pode ser `INNER JOIN`, `LEFT JOIN`, etc.) |
| **Renomeação (ρ)**             | Altera o nome de uma relação ou de suas colunas. | `AS` (para colunas e tabelas) |
| **Divisão (÷)**                | Retorna tuplas de uma relação que estão associadas a todas as tuplas de outra relação. | Não tem um equivalente direto em SQL, mas pode ser simulado com subconsultas e `GROUP BY` |

