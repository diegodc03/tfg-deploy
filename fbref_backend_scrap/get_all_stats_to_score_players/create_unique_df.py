
# This script is used to create a unique dataframe from a list of dataframes.
# It takes a list of Spark dataframes and combines them into a single dataframe.
def create_unique_df(spark_df):
    
    final_avg_dfs = spark_df[0]
    for df in spark_df[1:]:
        final_avg_dfs = final_avg_dfs.union(df)
    
    return final_avg_dfs
