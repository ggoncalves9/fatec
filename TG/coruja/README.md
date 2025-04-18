# 🦉 Projeto Coruja - MVP de Agente de Estudo via WhatsApp

Este é o projeto Coruja: um sistema que envia quizzes diários para alunos via WhatsApp, utilizando agentes inteligentes em Kubernetes. Este MVP será executado localmente, e depois migrado para AWS EKS.

## ✅ Etapas do Projeto

### 🧱 Etapa 1 - Ambiente Local (MVP)

- [x] Subir banco PostgreSQL via Docker Compose
- [ ] Criar estrutura de banco com tabelas: alunos, questões, histórico, usuários
- [ ] Criar agentes com CrewAI:
  - [ ] Validador de sessão
  - [ ] Gerador de perguntas
  - [ ] Avaliador de respostas
- [ ] Criar agente WhatsApp (mock)
- [ ] Agendamento via `cronjob` local (simulação)
- [ ] API REST para dashboard
- [ ] Dashboard com autenticação simples
- [ ] Coleta de métricas com Prometheus
- [ ] Logging com Loki
- [ ] Visualização com Grafana

### ☁️ Etapa 2 - Deploy em AWS EKS

- [ ] Infraestrutura com Terraform (VPC, RDS, EKS, IAM)
- [ ] Deploy de containers via Helm/manifestos
- [ ] Integração com serviço real de WhatsApp (ex: Twilio ou Gupshup)
- [ ] Monitoramento e segurança em produção

---

## 📁 Estrutura de Diretórios

```bash
coruja/
├── docker-compose.yaml
├── initdb/
│   └── init.sql
├── agents/
│   ├── validator.py
│   ├── question_generator.py
│   └── responder.py
├── whatsapp-bot/
│   └── bot.py
├── api/
│   ├── main.py
│   └── routes/
├── dashboard/
│   ├── app.py
│   └── templates/
├── jobs/
│   └── daily_quiz.py
├── observability/
│   ├── prometheus/
│   ├── grafana/
│   └── loki/
├── kubernetes/
│   ├── deployments/
│   ├── services/
│   ├── cronjobs/
│   └── secrets/
└── README.md
