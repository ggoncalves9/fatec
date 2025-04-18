-- Limpar dados existentes
TRUNCATE TABLE conquistas CASCADE;

-- Conquistas baseadas em pontuação
INSERT INTO conquistas (nome, descricao, criterio, icone) VALUES
('Iniciante', 'Respondeu corretamente sua primeira questão', 'Acertar a primeira questão', 'badge-bronze.png'),
('Aprendiz', 'Acumulou 100 pontos', 'Pontuação total >= 100', 'badge-silver.png'),
('Mestre', 'Acumulou 500 pontos', 'Pontuação total >= 500', 'badge-gold.png'),
('Lenda', 'Acumulou 1000 pontos', 'Pontuação total >= 1000', 'badge-platinum.png');

-- Conquistas baseadas em consistência
INSERT INTO conquistas (nome, descricao, criterio, icone) VALUES
('Dedicação', 'Respondeu questões por 7 dias consecutivos', '7 dias de atividade consecutiva', 'badge-streak.png'),
('Persistência', 'Respondeu questões por 30 dias consecutivos', '30 dias de atividade consecutiva', 'badge-marathon.png');

-- Conquistas baseadas em desempenho
INSERT INTO conquistas (nome, descricao, criterio, icone) VALUES
('Perfeccionista', 'Acertou 10 questões difíceis consecutivas', '10 acertos consecutivos em questões HARD', 'badge-perfect.png'),
('Versátil', 'Acertou questões em todos os níveis de dificuldade', 'Acertar pelo menos uma questão de cada nível', 'badge-versatile.png');

-- Conquistas baseadas em ranking
INSERT INTO conquistas (nome, descricao, criterio, icone) VALUES
('Top 10', 'Alcançou o top 10 do ranking mensal', 'Posição <= 10 no ranking mensal', 'badge-top10.png'),
('Campeão', 'Ficou em primeiro lugar no ranking mensal', 'Posição = 1 no ranking mensal', 'badge-champion.png'); 