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

    q1 = df['price'].quantile(0.25)
    q2 = df['price'].quantile(0.50)
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1

    print("\n=== Квартили и IQR ===")
    print(f"Q1 (25%): {q1:.2f} руб.")
    print(f"Q2 (50%): {q2:.2f} руб.")
    print(f"Q3 (75%): {q3:.2f} руб.")
    print(f"IQR (Q3 - Q1): {iqr:.2f} руб.")

    expensive_products = df[df['price'] > q3][['product_name', 'category', 'price']]
    print("\nТовары с ценой выше Q3:")
    print(expensive_products.to_string(index=False))

except Exception as error:
    print(f"Ошибка: {error}")

finally:
    if 'connection' in locals():
        connection.close()

        
