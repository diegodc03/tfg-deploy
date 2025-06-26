

def read_data_with_spark(spark, jdbc_url, db_properties, query):
    
    spark_df = spark.read.jdbc(
        url=jdbc_url, 
        table=f"({query}) as stats",
        properties=db_properties
    )
    
    return spark_df

