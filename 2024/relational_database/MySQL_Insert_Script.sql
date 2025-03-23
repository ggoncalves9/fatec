
-- Script para inserir dados das listas de MySQL

-- TP01 - MySQL
CREATE TABLE tb_vendas (
    cd_venda INT PRIMARY KEY,
    nm_curso VARCHAR(100),
    nm_aluno VARCHAR(100),
    estado VARCHAR(100),
    valor DECIMAL(10, 2)
);

INSERT INTO tb_vendas (cd_venda, nm_curso, nm_aluno, estado, valor) VALUES
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

-- TP02 - MySQL
CREATE TABLE tb_produto (
    cd_prod VARCHAR(10) PRIMARY KEY,
    ds_produto VARCHAR(50)
);

INSERT INTO tb_produto (cd_prod, ds_produto) VALUES
('101001', 'Java 8'),
('101002', 'Python 3,10'),
('101003', 'Iniciando HTML'),
('101004', 'Tutorial sobre SQL'),
('101005', 'Engenharia de Software'),
('333333', 'SQL Magazine'),
('333334', 'Python Magazine');

CREATE TABLE tb_venda (
    cd_venda VARCHAR(10) PRIMARY KEY,
    cd_produto VARCHAR(10),
    qt_produto INT,
    total DECIMAL(10, 2)
);

INSERT INTO tb_venda (cd_venda, cd_produto, qt_produto, total) VALUES
('200111', '090909', 6, 80.00),
('200112', '101001', 2, 140.00),
('200113', '101002', 1, 210.00),
('200114', '101003', 4, 120.00),
('200115', '080000', 1, 44.00),
('200116', '333333', 2, 50.00);

-- TP03 - MySQL
CREATE TABLE tb_clientes (
    id_cliente INT PRIMARY KEY,
    nm_cliente VARCHAR(50),
    sobrenome_cliente VARCHAR(50),
    data_nascimento DATE,
    estado_civil VARCHAR(1),
    genero VARCHAR(1),
    email VARCHAR(100),
    telefone VARCHAR(20),
    renda DECIMAL(10, 2),
    dependentes INT,
    escolaridade VARCHAR(50)
);

-- Dados da tabela de clientes já são muito extensos e devem ser adaptados conforme necessário.

CREATE TABLE tb_produtos (
    id_produto INT PRIMARY KEY,
    nm_produto VARCHAR(50),
    categoria INT,
    marca VARCHAR(50),
    codigo_produto VARCHAR(50),
    preco DECIMAL(10, 2),
    custo DECIMAL(10, 2)
);

INSERT INTO tb_produtos (id_produto, nm_produto, categoria, marca, codigo_produto, preco, custo) VALUES
(10, 'Microfone Condensador MC1000', 5, 'AKG', 'MIC-AK-237591', 1100, 275),
(11, 'Microfone Condensador com Tripé', 5, 'BLUE', 'MIC-BL-819455', 800, 344),
(12, 'Microfone de mesa com fio condensador', 5, 'BLUE', 'MIC-BL-761411', 650, 214.5);

-- TP04 - MySQL
CREATE TABLE tb_clientes (
    id_cliente INT PRIMARY KEY,
    nm_cliente VARCHAR(50),
    cid_cliente VARCHAR(50)
);

INSERT INTO tb_clientes (id_cliente, nm_cliente, cid_cliente) VALUES
(1, 'João Silva', 'São Paulo'),
(2, 'Maria Oliveira', 'Rio de Janeiro'),
(3, 'Pedro Santos', 'Belo Horizonte'),
(4, 'Ana Souza', 'Campinas'),
(5, 'Carla Maria', 'Indaiatuba'),
(6, 'André Santos', 'Salto'),
(7, 'Oscar Reinaldo', 'Itu'),
(8, 'Thiago Ricardo', 'Holambra');

CREATE TABLE tb_produtos (
    id_produto INT PRIMARY KEY,
    nm_produto VARCHAR(50),
    pre_produto DECIMAL(10, 2)
);

INSERT INTO tb_produtos (id_produto, nm_produto, pre_produto) VALUES
(101, 'Notebook', 3000.00),
(102, 'Teclado', 80.00),
(103, 'Mouse', 50.00),
(104, 'Monitor 14"', 600.00);

CREATE TABLE tb_vendas (
    id_venda INT PRIMARY KEY,
    id_cliente INT,
    id_produto INT,
    quantidade INT,
    data_venda DATE
);

INSERT INTO tb_vendas (id_venda, id_cliente, id_produto, quantidade, data_venda) VALUES
(1, 1, 101, 1, '2024-11-01'),
(2, 2, 102, 2, '2024-11-02'),
(3, 1, 103, 3, '2024-11-03');
