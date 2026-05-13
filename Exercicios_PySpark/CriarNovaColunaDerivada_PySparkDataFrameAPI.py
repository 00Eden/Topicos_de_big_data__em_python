from pyspark.sql.functions import col

# Criar coluna rooms_per_person
df_spark = df_spark.withColumn(
    "rooms_per_person",
    col("total_rooms") / col("population")
)

# Mostrar resultado
df_spark.show(5)
