# Usamos una imagen base con Python
FROM python:3.9-slim

# Instalar dependencias del sistema necesarias para Spark
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Configuración de Spark
ENV SPARK_VERSION=3.3.0
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Descargar y extraer Apache Spark
RUN wget -q https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    && tar -xvf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /opt \
    && mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark \
    && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Copiar los archivos de tus scripts al contenedor
COPY ./scripts /app/scripts

# Instalar dependencias de Python (por ejemplo, PySpark)
RUN pip install --no-cache-dir \
    pyspark \
    sqlalchemy \
    psycopg2-binary \
    pandas \
    && rm -rf /root/.cache

# Definir el directorio de trabajo
WORKDIR /app/scripts

# Comando por defecto
CMD ["python", "fbref_scrap.py"]
