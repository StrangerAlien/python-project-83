import psycopg2
from page_analyzer.secrets import DATABASE_URL
import os


def test_db():
    print('YO')


try:
    conn = psycopg2.connect(DATABASE_URL)
except:
    print('zalupa')

cursor = conn.cursor()
cursor.execute('SELECT * FROM urls')
all_users = cursor.fetchall()

print(all_users)

cursor.close()  # закрываем курсор
conn.close()  # закрываем соединение
