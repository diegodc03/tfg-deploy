




def write_dataframe_to_mysql(df, jdbc_url, db_properties, table_name):
    df.write \
        .format("jdbc") \
        .option("url", jdbc_url) \
        .option("dbtable", table_name) \
        .option("user", db_properties["user"]) \
        .option("password", db_properties["password"]) \
        .option("driver", db_properties["driver"]) \
        .option("batchsize", "10000") \
        .mode("append") \
        .save()