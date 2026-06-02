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
        pr.price,
        p.name AS product_name,
        p.category
    FROM prices pr
    JOIN products p
        ON pr.product_id = p.id
    """

    df = pd.read_sql_query(query, connection)

    by_category = df.groupby('category')['price'].agg(
        count='count',
        mean='mean',
        median='median',
        std='std'
    ).round(2).sort_values(by='mean', ascending=False)

    print(by_category)

except Exception as error:
    print(f"Ошибка: {error}")


        