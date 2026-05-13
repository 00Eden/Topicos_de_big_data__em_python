consulta_top5 = """
SELECT *
FROM housing_test
ORDER BY median_house_value DESC
LIMIT 5
"""

top5 = spark.sql(consulta_top5)

top5.show()
