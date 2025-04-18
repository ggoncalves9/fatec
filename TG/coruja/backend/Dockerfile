FROM python:3.11-bullseye

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq-dev \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
