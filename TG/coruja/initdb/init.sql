-- Criação da tabela de alunos
CREATE TABLE IF NOT EXISTS cad_aluno (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(150),
  curso VARCHAR(100),
  tema_estudo VARCHAR(50),
  score INTEGER DEFAULT 0
);

-- Criação da tabela de perguntas
CREATE TABLE IF NOT EXISTS cad_questoes (
  id_quest SERIAL PRIMARY KEY,
  pergunta TEXT NOT NULL,
  valor_score INTEGER DEFAULT 1,
  tema_estudo VARCHAR(50),
  dificuldade VARCHAR(10) CHECK (dificuldade IN ('EASY', 'MEDIUM', 'HARD'))
);

-- Histórico de respostas
CREATE TABLE IF NOT EXISTS historico_respostas (
  id SERIAL PRIMARY KEY,
  id_aluno INTEGER REFERENCES cad_aluno(id),
  id_quest INTEGER REFERENCES cad_questoes(id_quest),
  resposta_correta BOOLEAN,
  data_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Usuários para o dashboard
CREATE TABLE IF NOT EXISTS usuarios_dashboard (
  id SERIAL PRIMARY KEY,
  usuario VARCHAR(50) NOT NULL UNIQUE,
  senha_hash TEXT NOT NULL
);
