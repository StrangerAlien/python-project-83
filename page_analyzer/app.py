from flask import Flask, render_template
from page_analyzer.secrets import SECRET_KEY

from page_analyzer import actions_with_db as db


from datetime import datetime, timezone
from urllib.parse import urlparse

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/urls')
def urls():
    return render_template('test.html')


# @app.route('/')
# def home(url=''):
#     return render_template('index.html', url=url)
#
#
# @app.route('/urls', methods=['POST'])
# def test(url=''):
#     # добавляй в базу данных
#     add_new_url(conn, url)
#     return render_template('test.html', url=url)
#
#
# def add_new_url(conn, url):
#     """Create new name in database from url and return """
#     conn = psycopg2.connect(DATABASE_URL)
#     cursor = conn.cursor()
#     with conn.cursor() as cur:
#         cur.execute('INSERT INTO urls (name, created_at) VALUES (%s, %s) ;', (url, datetime.now()))
#
#     cursor.close()  # закрываем курсор
#     conn.close()
