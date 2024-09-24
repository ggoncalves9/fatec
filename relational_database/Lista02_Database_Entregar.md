1) Liste os nomes de todos os funcionários
consulta1 = pi Nome (tb_Empregado)

2) Liste o valor e a localização de todos os projetos
consulta2 = pi PValor, pi PLocal (tb_Projeto)

3) Liste o nome de todos os departamentos
consulta3 = pi DNome(tb_Departamento)

4) Encontre o nome, rg do responsável e a data de nascimento de todos os dependentes
consulta4 = pi DependNome,RGResp,Data_Nasc(tb_Dependente)

5) Encontre o nome de todos os empregados que possuem dependentes
consulta5 = pi Nome (σ tb_Empregado.RG=tb_Dependente.RGResp(tb_Dependente JOIN ⨝ tb_Empregado))

6) Encontre o nome e salário dos funcionários que recebem acima de 2000
pi Nome,Salario (σSalario>2000(tb_Empregado))

7) Consulte os nomes dos empregados que trabalham em todos os projetos controlados 
pelo departamento 2.
consulta7 = pi Nome(σDepto=2(tb_Empregado))

8) Encontre os nomes dos funcionários que não possuem dependentes
 pi Nome(tb_Dependente - pi Nome(tb_Empregados⨝tb_Dependente))

9) Para cada nome de empregado, obtenha o departamento que este gerencia.
   pi Nome,DNome(σRG = RG_Gerent(tb_Departamento ⋈ tb_Empregado))

10) Com o nome do empregado Ricardo, monte uma pesquisa utilizando a Álgebra
relacional que mostre os projetos que o funcionário participa.

 (σ Nome = Ricardo (tb_Empregado⋈(tb_Emp-tb_Proj))

11) Monte uma pesquisa em álgebra relacional utilizando o mesmo enunciado acima 
(enunciado, porém não utilizando a relação empregado_projeto.

 (σ Nome = Ricardo (tb_Empregado⋈(tb_Projeto⋈tb_Departamento))


13) Liste o nome dos gerentes que possuem dependentes. 
π Nome (σ tb_Empregado.RG=tb_Dependente.RGResp∧tb_Empregado.RG=tb_Departamento.RG_Gerent(tb_Empregado⋈tb_Dependente⋈tb_Departamento))

13) Selecione todos os empregados que trabalham no departamento número 2 ou que 
supervisionam empregados que trabalham no departamento número 2

π Nome (σ Depto=2 (tb_Empregado)∪π Nome (σ Depto=2 (tb_Empregado⋈tb_Empregado.RG_Gerent)))


1) d) Modelo relacional (SQL), NoSQL, rede e hierárquico

2) d) A operação de União entre duas tabelas A e B resulta em uma nova tabela que inclui todas as tuplas que estão em A e em B, simultaneamente.
Essa afirmação está incorreta porque a operação de união entre duas tabelas inclui as tuplas que estão em A ou B, e não simultaneamente.

3) d) restrição e projeção.

4) e) R |x| S.

5)b) projeção.

6)d) Os itens I, II e III são verdadeiros.

7)d) (1, N).
