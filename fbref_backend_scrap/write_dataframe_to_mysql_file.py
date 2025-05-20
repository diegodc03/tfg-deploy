
from bs4 import BeautifulSoup as soup
import requests
import time
import re
from functools import reduce
import sys
from urllib.error import HTTPError
import unicodedata
import multiprocessing
import math

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, ArrayType, FloatType, DoubleType
from pyspark.sql.functions import col, to_date
import numpy as np
import lxml





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