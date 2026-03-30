import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# Посмотреть таблицы
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Таблицы в базе:", cursor.fetchall())

# Посмотреть пользователей
cursor.execute("SELECT * FROM users;")
print("Пользователи:", cursor.fetchall())

# Посмотреть черный список
cursor.execute("SELECT * FROM blacklist;")
print("Черный список:", cursor.fetchall())

conn.close()