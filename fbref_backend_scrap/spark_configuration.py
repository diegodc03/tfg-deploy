
from pyspark.sql import SparkSession



# Configuración de conexión a MySQL
jdbc_url = "jdbc:mysql://localhost:3306/tfg_1_base_datos_partido_prueba"
db_properties = {
    "user": "root",
    "password": "",
    "driver": "com.mysql.cj.jdbc.Driver", 
}

# Función para crear el SparkSession
def create_spark_session():
    print("Creando Spark Session...")
    spark = SparkSession.builder \
        .appName("FootballMatchLoader") \
        .config("spark.driver.extraClassPath", r"C:\spark\jars\mysql-connector-j-9.2.0.jar") \
        .getOrCreate()
    
    print("Spark Session creada con configuración:")
    print(spark.conf.get("spark.driver.extraClassPath"))

    return spark

