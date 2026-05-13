consulta = """
SELECT *
FROM housing_test
WHERE median_house_value > 450000
AND median_income > 10
LIMIT 5
"""

resultado = spark.sql(consulta)

resultado.show()
