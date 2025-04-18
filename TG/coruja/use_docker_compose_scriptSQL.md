🚀 Instruções para Rodar
1. Crie a estrutura de diretórios:

```
mkdir coruja && cd coruja
mkdir initdb
touch docker-compose.yaml initdb/init.sql
```
2. Cole os conteúdos acima nos arquivos correspondentes.
3. Rode o container:
```
docker-compose up -d
```
4. Verifique se está funcionando:

```
docker exec -it coruja_postgres psql -U coruja_user -d coruja_db
```
