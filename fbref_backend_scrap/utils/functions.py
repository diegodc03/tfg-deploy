
from get_average_stats.fbref_get_average_stats_by_specific_position import loop_throgh_all_columns_basic_positions

def introduce_in_data(data, *dict):
    for d in dict:
        data.append(tuple(d.values())) 
        
def fill_stats_dict(spark_df, expected_columns, dict_avg, dict_desv, dict_mode):
    count = spark_df.count()
    if count > 0:
        avg, max, mode = loop_throgh_all_columns_basic_positions(spark_df, count)
        dict_avg.update(avg)
        dict_desv.update(max)
        dict_mode.update(mode)
                        
    else:
        for col in expected_columns:
            if col not in dict_avg:
                dict_avg[col] = 0.0
                dict_desv[col] = 0.0
                dict_mode[col] = 0.0
                                
 

       