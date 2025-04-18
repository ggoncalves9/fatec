-- Limpar dados existentes
TRUNCATE TABLE cad_questoes CASCADE;

-- EASY
INSERT INTO cad_questoes (pergunta, valor_score, tema_estudo, dificuldade, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta, explicacao) VALUES
('Qual comando exibe o diretório atual no Linux?', 1, 'Linux', 'EASY', 
'pwd', 'ls', 'cd', 'mkdir', 'A',
'O comando pwd (print working directory) exibe o diretório atual no Linux.'),

('Qual comando exibe os pods em execução no Kubernetes?', 1, 'Kubernetes', 'EASY',
'kubectl get pods', 'kubectl list pods', 'kubectl show pods', 'kubectl pods list', 'A',
'O comando kubectl get pods lista todos os pods em execução no cluster.');

-- MEDIUM
INSERT INTO cad_questoes (pergunta, valor_score, tema_estudo, dificuldade, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta, explicacao) VALUES
('Qual comando remove um diretório no Linux, mesmo que ele tenha arquivos?', 2, 'Linux', 'MEDIUM',
'rm -rf', 'rmdir', 'rm -r', 'rm -d', 'A',
'O comando rm -rf remove recursivamente (-r) e forçadamente (-f) um diretório e todo seu conteúdo.'),

('Qual é o arquivo padrão de configuração do kubelet?', 2, 'Kubernetes', 'MEDIUM',
'/var/lib/kubelet/config.yaml', '/etc/kubernetes/kubelet.conf', '/etc/kubelet/config.yaml', '/var/lib/kubelet/kubelet.conf', 'A',
'O arquivo /var/lib/kubelet/config.yaml é o local padrão para a configuração do kubelet.');

-- HARD
INSERT INTO cad_questoes (pergunta, valor_score, tema_estudo, dificuldade, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta, explicacao) VALUES
('Como funciona o mecanismo de Cgroups no Linux para gerenciamento de recursos?', 3, 'Linux', 'HARD',
'Isola e limita o uso de recursos do sistema por grupos de processos', 'Gerencia a memória virtual do sistema', 'Controla o acesso a dispositivos de hardware', 'Gerencia as permissões de arquivos', 'A',
'Cgroups (Control Groups) é um mecanismo do kernel Linux que isola e limita o uso de recursos do sistema por grupos de processos.'),

('Explique a diferença entre Deployment e StatefulSet no Kubernetes.', 3, 'Kubernetes', 'HARD',
'Deployment é para aplicações stateless, StatefulSet para stateful', 'Deployment é mais rápido que StatefulSet', 'StatefulSet é mais simples que Deployment', 'Não há diferença significativa', 'A',
'Deployment é usado para aplicações stateless onde a ordem e identidade dos pods não importa, enquanto StatefulSet é usado para aplicações stateful que precisam de identidade estável e ordem de inicialização.'); 