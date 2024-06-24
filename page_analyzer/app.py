from flask import Flask, render_template
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')


@app.route('/')
def hello_python_project_83():
    return render_template('index.html')


# url_connect = 'postgresql://hexlet:hexlet@localhost/sites'

try:
    # conn = psycopg2.connect(dbname="sites", host="localhost", user="hexlet", password="hexlet")
    conn = psycopg2.connect(DATABASE_URL)
    # print(conn)
except:
    print('zalupa')

cursor = conn.cursor()
cursor.execute('SELECT * FROM urls')
all_users = cursor.fetchall()

print(all_users)

cursor.close()  # закрываем курсор
conn.close()  # закрываем соединение
