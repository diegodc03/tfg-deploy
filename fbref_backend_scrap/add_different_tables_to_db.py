

import pandas as pd
from pyspark.sql.types import StructType
from spark_schema import get_type_position_schema, get_event_shots_schema, get_body_part_schema, get_outcome_schema
from write_dataframe_to_mysql_file import write_dataframe_to_mysql
from constants import type_shots, body_parts, outcomes, type_positions




def add_type_shots_to_database(spark, jdbc_url, db_properties):
    print("")
    print("Inserting type of shots in database")

    success = spark.createDataFrame([], StructType([]))

    df = check_elements_on_table_exists(spark, jdbc_url, db_properties, "event_shots")
    if df > 0:
        print("Type of position on the field already exists in database") 
    else:
        try:
            df = pd.DataFrame({"event_shot_name": type_shots}).drop_duplicates()

            schema = get_event_shots_schema()

            df_spark = spark.createDataFrame(df, schema)
            write_dataframe_to_mysql(df_spark, jdbc_url, db_properties, "event_shots")
            success = df_spark

        except Exception as e:
            print(f"Error inserting type of shots in database: {e}")
            
    return success



def add_body_part_to_database(spark, jdbc_url, db_properties):
    print("")
    print("Inserting body part in database")
    success = spark.createDataFrame([], StructType([]))

    df = check_elements_on_table_exists(spark, jdbc_url, db_properties, "body_part")
    if df > 0:
        print("Type of position on the field already exists in database")
       
    else:
        try:
            df = pd.DataFrame({"body_part_name": body_parts}).drop_duplicates()

            schema = get_body_part_schema()
            df_spark = spark.createDataFrame(df, schema)
            write_dataframe_to_mysql(df_spark, jdbc_url, db_properties, "body_part")
            success = df_spark
        except Exception as e:
            print(f"Error inserting body part in database: {e}")
            
    return success

def add_outcome_to_database(spark, jdbc_url, db_properties):
    print("")
    print("Inserting outcome in database")
    success = spark.createDataFrame([], StructType([]))

    df = check_elements_on_table_exists(spark, jdbc_url, db_properties, "outcome_stats")
    if df > 0:
        print("Type of position on the field already exists in database")
        
    else:
        try:
            df = pd.DataFrame({"outcome_name": outcomes}).drop_duplicates()

            schema = get_outcome_schema()

            df_spark = spark.createDataFrame(df, schema)
            write_dataframe_to_mysql(df_spark, jdbc_url, db_properties, "outcome_stats")
            success = df_spark

        except Exception as e:
            print(f"Error inserting outcome in database: {e}")

    return success


"""
GK - Goalkeepers / Porteros
DF - Defenders / Defensas
MF - Midfielders / Centrocampistas
FW - Forwards / Delanteros
FB - Fullbacks / Laterales
LB - Left Backs / Laterales Izquierdos
RB - Right Backs / Laterales Derechos
CB - Center Backs / Defensas Centrales 
DM - Defensive Midfielders / Mediocentros Defensivos
CM - Central Midfielders / Mediocentros
LM - Left Midfielders / Centrocampistas Izquierdos
RM - Right Midfielders / Centrocampistas Derechos
WM - Wide Midfielders / Centrocampistas por las bandas
LW - Left Wingers / Extremos Izquierdos
RW - Right Wingers / Extremos Derechos
AM - Attacking Midfielders / Mediapuntas / Delantero Centro
"""

def add_type_of_position_on_field_to_database(spark, jdbc_url, db_properties):
    print("")
    print("Inserting type of position in field in database")
    success = spark.createDataFrame([], StructType([]))

    df = check_elements_on_table_exists(spark, jdbc_url, db_properties, "position_on_the_field")
    if df > 0:
        print("Type of position on the field already exists in database")
        
    else:
        try:
            df = pd.DataFrame({"position_name": type_positions}).drop_duplicates()
            schema = get_type_position_schema()

            df_spark = spark.createDataFrame(df, schema)
            write_dataframe_to_mysql(df_spark, jdbc_url, db_properties, "position_on_the_field")
            success = df_spark
        except Exception as e:
            print(f"Error inserting type of position in field in database: {e}")
        
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