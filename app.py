import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user="postgres",
                            password="0611")
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "books";')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)


if __name__ == '__main__':
    app.run()
