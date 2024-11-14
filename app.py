import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="gitinovasov",
    user="mahach",
    password="mahach",
    host="postgres_mahach"  # Название сервиса контейнера PostgreSQL внутри Docker Compose
)
cur = conn.cursor()

# Выполнение запроса
query = """
SELECT MIN(age) AS min_age, MAX(age) AS max_age
FROM test_table
WHERE LENGTH(name) < 6
"""
cur.execute(query)
result = cur.fetchone()

# Вывод результатов
print("Минимальный возраст для имен менее 6 символов:", result[0])
print("Максимальный возраст для имен менее 6 символов:", result[1])

# Закрытие курсора и соединения
cur.close()
conn.close()