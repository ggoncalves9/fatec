FROM nginx:stable-alpine

# Criar diretório para os arquivos estáticos
RUN mkdir -p /usr/share/nginx/html

# Copiar os arquivos estáticos
COPY public/ /usr/share/nginx/html/

# Copiar a configuração do nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Configurar permissões
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
