-- Criar tabela de usuários se não existir
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    ultimo_login TIMESTAMP,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Limpar dados existentes
DELETE FROM usuarios WHERE email IN ('admin@admin.com', 'teste@teste.com');

-- Inserir usuários (senha em bcrypt hash)
INSERT INTO usuarios (nome, email, senha_hash) VALUES
('Administrador', 'admin@admin.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewFpxQgkj6PM7Y2e'), -- senha: owl123
('Teste', 'teste@teste.com', '$2b$12$QJqf.CGX7jDWd8zRHkHNxOPYr6M3qZvX9D6d5Jt9gzOGV.qXQG9Gy'); -- senha: 123 