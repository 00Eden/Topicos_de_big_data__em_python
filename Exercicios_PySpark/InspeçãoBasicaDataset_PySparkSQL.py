# Mostrar esquema
df_spark.printSchema()

# Contagem de linhas
print("Quantidade de linhas:")
print(df_spark.count())

# Estatísticas básicas
df_spark.describe().show()
