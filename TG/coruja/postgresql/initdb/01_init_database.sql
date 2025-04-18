-- Criar o banco de dados se não existir
SELECT 'CREATE DATABASE coruja'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'coruja');

-- Conectar ao banco de dados coruja
\c coruja;

-- Habilitar extensões necessárias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Criar schemas
CREATE SCHEMA IF NOT EXISTS public;
COMMENT ON SCHEMA public IS 'Schema padrão do banco de dados';

-- Configurar timezone
SET timezone = 'America/Sao_Paulo'; 