# Normalização Objetivo

1 eliminar a redundância de dados

Normalização passaos

ma relacional normalizado

esquema de arquivos ou documento
representação como tabela Ñn
esquie,a não normalizado 
passagem a 1FN 

Roteiro

ÑN forma nãp mormaçizada
esquema 1Fn P


#


## Chave candidata - Forma normal de boyce-codd (FNBC)
Ex: RA, RG, CPG, tel, CNH, passaporte, e-mail, numero do sus

Encontrar qual dado referente a regra do negocio tem valor para ser utilizada dentro do projeto

## Tipos de relacionamentos
Unário - utilizando o auto relacionamento

Binario

Ternario


# Explicação de Chaves e Relacionamentos
### Bancos de Dados Relacionais

---
## Tipos de Chave

### Chave Primária (Primary Key)
- **O que é**: Identifica unicamente cada registro em uma tabela.
- **Exemplo**: `ID do Cliente` na tabela `Clientes`.

### Chave Estrangeira (Foreign Key)
- **O que é**: Referencia a chave primária de outra tabela.
- **Exemplo**: `ID do Cliente` na tabela `Pedidos`, referenciando `Clientes`.

### Chave Candidata (Candidate Key)
- **O que é**: Pode ser uma chave primária, pois identifica unicamente um registro.
- **Exemplo**: `CPF` ou `Número de Registro` na tabela `Funcionários`.

### Chave Composta (Composite Key)
- **O que é**: Chave primária formada por mais de um atributo.
- **Exemplo**: Combinação de `ID do Aluno` e `ID do Curso` na tabela `Inscrições em Cursos`.

### Chave Alternativa (Alternate Key)
- **O que é**: Chave candidata que não foi escolhida como chave primária.
- **Exemplo**: `CPF` se não for a chave primária.

## Tipos de Relacionamento

### Relacionamento Unário
- **O que é**: Relacionamento entre instâncias da mesma entidade.
- **Exemplo**: Funcionário supervisionando outros funcionários na tabela `Funcionários`.

### Relacionamento Binário
- **O que é**: Relacionamento entre duas entidades diferentes.
- **Exemplo**: `Clientes` e `Pedidos`, onde um cliente pode fazer vários pedidos.

### Relacionamento Ternário
- **O que é**: Relacionamento envolvendo três entidades diferentes.
- **Exemplo**: `Professores`, `Alunos` e `Cursos`, onde um professor ensina um curso para vários alunos.

---

Esses conceitos são essenciais para a modelagem de bancos de dados relacionais, garantindo a integridade e eficiência dos dados.

---

A informação/dado inserio no banco de dados tem como filtro a regra de negocio para normalizar o dados

1 esquema ÑN
2 1FN
3 2FN
4 3FN

Desenhar o esquema MER e DER em base a proposta de negocio da empresa/alvo e normalizar os esquemas do database

Tabela ÑN esquema - é efetuada a organização das tabelas, aninhadando os dados, porem não é efetuado a modificação e sim a fragmentação

1FN apos fragmentar as tabelas em niveis de aninhamento

ex:
ÑN
(CodProj, Tipo, Descr,
  (CodProj, CodEmp, Nome, Cat, Sal, DataIni, Temal))
1FN
(CodProj,Tipo,Descr)


Dependecia funcional 2Fn e 3Fn
- total - fica totalmente dependente
- parcial -  existe dependencia entre os campos

Observação Codigo para Esquema

2FN
perdi as observaçoes rs
Emp (CodEmp,Nome, Cat, Sal)
--> CodEmp para Nome
--> CodEmp para Cat

dependencia total ou parcial


3FN
Emp (CodEmp, Nome, Cat)
dependencia transitiva


tabelas na 3FN e DER 
projeto - <projEmp> -  empregado - <> - categoria 

projeto - cod_proj, tipo, clase
ProjEmp - temporal,dataIn
Emp - cod_emp,nome
categoria - cat, salario

