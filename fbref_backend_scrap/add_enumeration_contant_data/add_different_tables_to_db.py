

import pandas as pd
from pyspark.sql.types import StructType
from fbref_backend_scrap.utils.write_dataframe_to_mysql_file import write_dataframe_to_mysql
from fbref_backend_scrap.utils.read_dataframe_to_mysql_file import read_data_with_spark


def insert_reference_data(spark, jdbc_url, db_properties, table_name, column_name, data_list, schema_function):
    print(f"\nInserting data into table: {table_name}")
    success = spark.createDataFrame([], StructType([]))

    df = check_elements_on_table_exists(spark, jdbc_url, db_properties, table_name)
    if df > 0:
        print(f"Data already exists in table {table_name}")
    else:
        try:
            df = pd.DataFrame({column_name: data_list}).drop_duplicates()
            schema = schema_function()
            df_spark = spark.createDataFrame(df, schema)
            write_dataframe_to_mysql(df_spark, jdbc_url, db_properties, table_name)
            success = df_spark
        except Exception as e:
            print(f"Error inserting into table {table_name}: {e}")

    return success




def insert_categories(spark, jdbc_url, db_properties):
    categories = ["goalkeepers", "defenders", "midfielders", "forwards"]
    
    existing_categories = spark.read.jdbc(url=jdbc_url, table="position_category", properties=db_properties)
    
    if existing_categories.count() == 0:
        df = pd.DataFrame({"category_name": categories})
        df_spark = spark.createDataFrame(df)
        df_spark.write.jdbc(url=jdbc_url, table="position_category", mode="append", properties=db_properties)
        print("Inserted categories into position_category")
    else:
        print("Categories already exist, skipping insert.")



def add_basic_position_to_database(spark, jdbc_url, db_properties):
    # Esta función añade las posiciones básicas de los jugadores a la base de datos
    print("Adding basic positions to database")
    try:
       
        
        #write_dataframe_to_mysql(df, jdbc_url, db_properties, "basic_position")
        print("Basic positions added successfully")
    except Exception as e:
        print(f"Error adding basic positions: {e}")
        
def add_specific_position_to_database(spark, jdbc_url, db_properties):
    # Esta función añade las posiciones específicas de los jugadores a la base de datos
    print("Adding specific positions to database")
    try:
        
        
        print("Specific positions added successfully")
    except Exception as e:
        print(f"Error adding specific positions: {e}")
        

def add_basic_game_modes_to_database(spark, jdbc_url, db_properties):
    # Esta función añade los tipos de posiciones básicas de los jugadores a la base de datos
    print("Adding basic type positions to database")
    try:
        
        
        print("Basic type positions added successfully")
    except Exception as e:
        print(f"Error adding basic type positions: {e}")
        
        
def add_specific_game_modes_to_database(spark, jdbc_url, db_properties):
    # Esta función añade los tipos de posiciones específicas de los jugadores a la base de datos
    print("Adding specific type positions to database")
    try:
        
        
        print("Specific type positions added successfully")
    except Exception as e:
        print(f"Error adding specific type positions: {e}")



def check_elements_on_table_exists(spark, jdbc_url, db_properties, table_name):
    try:
        df = spark.read \
            .format("jdbc") \
            .option("url", jdbc_url) \
            .option("dbtable", table_name) \
            .option("user", db_properties["user"]) \
            .option("password", db_properties["password"]) \
            .option("driver", db_properties["driver"]) \
            .load()

        return df.count()

    except Exception as e:
        print(f"Error checking table {table_name}: {e}")
        return 0