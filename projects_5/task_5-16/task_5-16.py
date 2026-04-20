import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5433",
        user="postgres_task",
        password="student",
        database="student"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT name, category FROM products;")
    products = cursor.fetchall()
   

    for product in products:
        print(f"Товар: {product[0]}, категория: {product[1]}")
    

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Ошибка при подключении: {error}")
