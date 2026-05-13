file_path_spark = 'file:///content/sample_data/california_housing_test.csv'

# Ler CSV
df_spark = spark.read.csv(
    file_path_spark,
    header=True,
    inferSchema=True
)

# Criar view temporária
df_spark.createOrReplaceTempView("housing_test")

print("View temporária criada com sucesso!")
