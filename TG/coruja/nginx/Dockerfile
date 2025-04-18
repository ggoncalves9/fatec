FROM nginx:stable-alpine

# Remove default nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Create directory for logs
RUN mkdir -p /var/log/nginx && \
    chown -R nginx:nginx /var/log/nginx

# Set proper permissions
RUN chown -R nginx:nginx /etc/nginx && \
    chmod -R 755 /etc/nginx

# Expõe a porta 80
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"] 