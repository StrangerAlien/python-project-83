import psycopg2
from page_analyzer.secrets import DATABASE_URL
from datetime import datetime


def connect_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
    except Exception as error:
        print('Can`t establish connection to database')
        raise error
    return conn


def save_url(url):
    conn = connect_db()
    with conn.cursor() as curs:
        curs.execute(
            'INSERT INTO urls (name, created_at) VALUES (%s, %s) RETURNING id;',
            (url, datetime.now()))
        url_data = curs.fetchone()
        conn.commit()
    return url_data[0]


def get_data_by_id(url_id):
    conn = connect_db()
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM urls WHERE id=%s', (url_id,))
        return curs.fetchone()


def get_data_all_urls():
    conn = connect_db()
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM urls ORDER BY id DESC;')
        return curs.fetchall()
