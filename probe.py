import sqlite3

path = 'https://sqliteonline.com/'
connection = sqlite3.connect(path)

cursor = connection.cursor()

cursor.execute('SELECT * FROM demo')

posts = cursor.fetchall()

for post in posts:
    print(post)

# Заполнение таблицы Users
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f"User{i}", f"example{i}@gmail.com", 10 * i, 1000))

# Обновление balance у каждой 2ой записи начиная с 1ой на 500:
# n = 1
# for i in range(1, 11):
#     if n == 1:
#         cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f"User{i}"))
#         n = 0
#     else:
#         n += 1

# Удаление каждой 3ей записи в таблице начиная с 1ой:
# n = 2
# for i in range(1, 11):
#     if n == 2:
#         cursor.execute('DELETE FROM Users WHERE username = ?', (f"User{i}",))
#         n = 0
#     else:
#         n += 1

# Выборка всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
# cursor.execute('SELECT username, email, age, balance FROM Users;')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()