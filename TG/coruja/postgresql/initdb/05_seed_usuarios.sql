-- Limpar dados existentes
TRUNCATE TABLE usuarios CASCADE;

-- Inserir usuários (senha em bcrypt hash)
INSERT INTO usuarios (nome, email, senha_hash) VALUES
('Administrador', 'admin@admin.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewFpxQgkj6PM7Y2e'), -- senha: owl123
('Teste', 'teste@teste.com', '$2b$12$QJqf.CGX7jDWd8zRHkHNxOPYr6M3qZvX9D6d5Jt9gzOGV.qXQG9Gy'); -- senha: 123 