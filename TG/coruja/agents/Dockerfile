FROM python:3.11-slim

WORKDIR /app

COPY question_selector.py .
COPY cronjob.txt /etc/cron.d/cronjob

# Instala cron + dependências
RUN apt-get update && \
    apt-get install -y cron && \
    pip install --no-cache-dir psycopg2-binary && \
    chmod 0644 /etc/cron.d/cronjob && \
    crontab /etc/cron.d/cronjob

# Cria log do cron
RUN touch /var/log/cron.log

# Verifica se o script Python existe e é executável
RUN chmod +x question_selector.py

# Adiciona verificação de saúde
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD ps aux | grep cron | grep -v grep || exit 1

CMD ["cron", "-f"]
