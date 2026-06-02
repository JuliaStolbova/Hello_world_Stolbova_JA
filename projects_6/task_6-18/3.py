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
        pr.price
    FROM prices pr
    """

    df = pd.read_sql_query(query, connection)

    metrics = {
        'Среднее (mean)': df['price'].mean(),
        'Медиана (median)': df['price'].median(),
        'Ст. отклонение (std)': df['price'].std(),
        'Минимум (min)': df['price'].min(),
        'Максимум (max)': df['price'].max(),
    }

    print("\n=== Метрики вручную ===")
    for name, val in metrics.items():
        print(f"{name:25s}: {val:.2f} руб.")

except Exception as error:
    print(f"Ошибка: {error}")


        

