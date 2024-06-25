import psycopg2
from page_analyzer.secrets import DATABASE_URL
from datetime import datetime


def connect_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except:
        print('Can`t establish connection to database')


def save_url(url):
    conn = connect_db()
    with conn.cursor() as curs:
        curs.execute('INSERT INTO urls (name, created_at) VALUES (%s, %s);', (url, datetime.now()))
        conn.commit()
