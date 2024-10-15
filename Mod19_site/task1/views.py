from django.shortcuts import render
# import sqlite3

from task1.models import Post


# Create your views here.
# def update_db(request):
#     path = 'sqlite.db'
#     connection = sqlite3.connect(path)
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM demo')
#     posts = cursor.fetchall()
#     for post in posts:
#         Post.objects.create(title=post[1], hint=post[2])
#     connection.commit()
#     connection.close()
