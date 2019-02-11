import os
import psycopg2
import psycopg2.extras


conn = None
cur = None


def connect():
    pass


def disconnect():
    pass


def select():
    pass


def insert(pylighter_input):
    pass


def delete(pylighter_input):
    pass
































def create_table():
    cur.execute('''
    CREATE TABLE attendance (
        id SERIAL PRIMARY KEY,
        name TEXT
    );
    ''')


def drop_table():
    cur.execute('''
    DROP TABLE attendance;
    ''')


def check_if_attendance_table_exists():
    cur.execute('''
    SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name = 'attendance');
    ''')
    table_exists = cur.fetchone()
    return table_exists
