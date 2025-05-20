# Dockerfile
FROM python:3.10.12-slim

ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir /backend_football_stats
WORKDIR /backend_football_stats

COPY requirements.txt /backend_football_stats/

RUN python -m pip install -r requirements.txt

COPY . /backend_football_stats



## Cuando haya que hacer el build de producción, comentar la siguiente línea
# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
