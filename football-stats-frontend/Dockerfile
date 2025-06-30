# Etapa 1: Build de la app
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Etapa 2: Servir la app estática con nginx
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

# Copia el config de nginx para SPA (ver siguiente paso)
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
