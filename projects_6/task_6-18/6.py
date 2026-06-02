import psycopg2
import pandas as pd

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres_task",
        password="student",
        database="student"
    )
    print("✓ Подключение установлено")

    query = """
    SELECT
        p.name AS product_name,
        p.category,
        MIN(pr.price) AS min_price,
        MAX(pr.price) AS max_price,
        MAX(pr.price) - MIN(pr.price) AS price_diff
    FROM prices pr
    JOIN products p
        ON pr.product_id = p.id
    GROUP BY p.name, p.category
    ORDER BY price_diff DESC
    LIMIT 5
    """

    df = pd.read_sql_query(query, connection)
    print(df)

except Exception as error:
    print(f"Ошибка: {error}")


        