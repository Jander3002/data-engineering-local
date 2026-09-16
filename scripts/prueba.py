import pandas as pd
from pyspark.sql import SparkSession

# Prueba básica de Pandas
df = pd.DataFrame({"Proyecto": ["Pipeline S3", "ETL SQL"], "Estado": ["OK", "OK"]})
print("--- Test Pandas ---")
print(df)

# Prueba básica de PySpark
spark = SparkSession.builder.appName("LocalTest").getOrCreate()
spark_df = spark.createDataFrame([("AWS", "S3"), ("Azure", "ADLS")], ["Cloud", "Storage"])
print("\n--- Test PySpark ---")
spark_df.show()