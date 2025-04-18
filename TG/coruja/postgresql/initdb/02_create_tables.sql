-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    id_random UUID DEFAULT uuid_generate_v4(),
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_login TIMESTAMP
);

-- Tabela de questões
CREATE TABLE IF NOT EXISTS cad_questoes (
    id_quest SERIAL PRIMARY KEY,
    id_random UUID DEFAULT uuid_generate_v4(),
    pergunta TEXT NOT NULL,
    valor_score INTEGER NOT NULL,
    tema_estudo VARCHAR(50) NOT NULL,
    dificuldade VARCHAR(10) NOT NULL CHECK (dificuldade IN ('EASY', 'MEDIUM', 'HARD')),
    opcao_a TEXT NOT NULL,
    opcao_b TEXT NOT NULL,
    opcao_c TEXT NOT NULL,
    opcao_d TEXT NOT NULL,
    resposta_correta CHAR(1) NOT NULL CHECK (resposta_correta IN ('A', 'B', 'C', 'D')),
    explicacao TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de respostas dos usuários
CREATE TABLE IF NOT EXISTS respostas_usuarios (
    id SERIAL PRIMARY KEY,
    id_random UUID DEFAULT uuid_generate_v4(),
    usuario_id INTEGER REFERENCES usuarios(id),
    questao_id INTEGER REFERENCES cad_questoes(id_quest),
    resposta CHAR(1) NOT NULL CHECK (resposta IN ('A', 'B', 'C', 'D')),
    pontuacao INTEGER NOT NULL,
    data_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de conquistas/badges
CREATE TABLE IF NOT EXISTS conquistas (
    id SERIAL PRIMARY KEY,
    id_random UUID DEFAULT uuid_generate_v4(),
    nome VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL,
    criterio TEXT NOT NULL,
    icone VARCHAR(100)
);

-- Tabela de conquistas dos usuários
CREATE TABLE IF NOT EXISTS conquistas_usuarios (
    id SERIAL PRIMARY KEY,
    id_random UUID DEFAULT uuid_generate_v4(),
    usuario_id INTEGER REFERENCES usuarios(id),
    conquista_id INTEGER REFERENCES conquistas(id),
    data_conquista TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de pontuações mensais
CREATE TABLE IF NOT EXISTS pontuacoes_mensais (
    id SERIAL PRIMARY KEY,
    id_random UUID DEFAULT uuid_generate_v4(),
    usuario_id INTEGER REFERENCES usuarios(id),
    mes INTEGER NOT NULL CHECK (mes BETWEEN 1 AND 12),
    ano INTEGER NOT NULL,
    pontuacao_total INTEGER DEFAULT 0,
    posicao_ranking INTEGER,
    UNIQUE(usuario_id, mes, ano)
);

-- Índices para melhor performance
CREATE INDEX IF NOT EXISTS idx_respostas_usuario ON respostas_usuarios(usuario_id);
CREATE INDEX IF NOT EXISTS idx_respostas_questao ON respostas_usuarios(questao_id);
CREATE INDEX IF NOT EXISTS idx_pontuacoes_usuario ON pontuacoes_mensais(usuario_id);
CREATE INDEX IF NOT EXISTS idx_pontuacoes_mes_ano ON pontuacoes_mensais(mes, ano); 