# syntax=docker/dockerfile:1

# --- Etapa 1: Build del proyecto ---
    FROM node:20-alpine AS builder

    WORKDIR /app
    
    # Copiar solo los archivos necesarios primero para aprovechar cache de Docker
    COPY package.json package-lock.json ./
    RUN npm ci
    
    # Copiar el resto de la aplicación
    COPY . .
    
    # Compilar el frontend
    RUN npm run build
    
    # --- Etapa 2: Servir la app estática ---
    FROM nginx:stable-alpine AS production
    
    # Copiar el resultado del build al contenedor de nginx
    COPY --from=builder /app/dist /usr/share/nginx/html
    
    # Copiar un archivo de configuración de nginx personalizado (opcional)
    # COPY nginx.conf /etc/nginx/nginx.conf
    
    EXPOSE 80
    
    # Arrancar nginx
    CMD ["nginx", "-g", "daemon off;"]
    