algebra relacional 
intersecção e uniao 

consultas

natura join 


---
	

1) Consulta1 = σ dnum>=1(tb_Departamento);

DNome | DNum | RG_Gerent
--- | --- | ---
Contabil | 1 | 101010
Eng.Civil | 2 | 303030
Eng.Mecânica | 3 | 202020


2) Consulta2 = σ rg_gerent=101010(tb_Empregado);

Nome | RG | CIC | Dept | RG_Gerent | Salario
--- | --- |--- |--- |--- |--- 
Fernando 202020 222222 2 101010 2.500,00
Ricardo 303030 333333 3 101010 2.300,00

3) Consulta3 = pi nome, rg (σ salario <= 2500(tb_Empregado));

Nome | RG 
--- | ---
Fernando | 202020 
Ricardo | 303030 

4) Consulta4 = pi dept_num(tb_Depart-tb_Proj);

Dept_Num |
--- |
2 	
3
2

5) Consulta5 = pi rg_emp,num_proj (σ horas=35 (tb_Emp-tb_Proj);

RG_Emp | Num_Proj
--- | --- 
303030 |5 

6) Consulta6 = pi depennome( σ rgresp=202020 ( σ sexo="m" (tb_Dependente) ) );

DependNome | 
--- |  
Angelo |


7) Consulta7a= pi nome (tb_Empregado);

Nome 
--- |            
Joao Luiz
Fernando
Ricardo 
Jorge


8) Consulta7b= pi dependnome (tb_Dependente);

DependNome
--- |
Jorge 
Luiz
Fernanda
Angelo
Adreia

9) Consulta7c= Consulta7a U Consulta7b;

Nome |DependNome
--- | ---         
Joao Luiz | Jorge
Joao Luiz | Luiz
Fernando | Fernanda
Ricardo | Andreia
Jorge |


10) Consulta8 = tb_Emp-tb_Proj X tb_Projeto;
11) Consulta9 = tb_Rmpregado |X| rg=rgresp (tb_Dependente)
