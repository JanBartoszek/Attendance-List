import os
import psycopg2
import psycopg2.extras

conn = psycopg2.connect("dbname={dbname} user={user} password={password} host={host}".format(
        dbname=os.environ.get("DBNAME"),
        user=os.environ.get("USER"),
        host=os.environ.get("HOST"),
        password=os.environ.get("PASSWORD")
    ))
conn.autocommit = True
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def insert(pylighter_input):
    cur.execute('''
    INSERT INTO attendance (name) VALUES (%s);
    ''', (pylighter_input,))


def delete(pylighter_input):
    cur.execute('''
    DELETE FROM attendance
    WHERE id = %s;
    ''', (pylighter_input,))


def select():
    cur.execute('''
    SELECT id, name, ROW_NUMBER () OVER (ORDER BY id) FROM attendance;
    ''')
    stuff = cur.fetchall()
    return stuff


def create_table():
    cur.execute('''
    CREATE TABLE attendance (
        id serial PRIMARY KEY,
        name TEXT
    );
    ''')


def drop_table():
    cur.execute('''
    DROP TABLE attendance;
    ''')
