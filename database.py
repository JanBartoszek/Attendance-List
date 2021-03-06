import os
import psycopg2
import psycopg2.extras


conn = None
cur = None


def connect():
    global conn, cur
    conn = psycopg2.connect("dbname={dbname} user={user} password={password} host={host}".format(
        dbname=os.environ.get("ATTENDANCE_LIST_DBNAME"),
        user=os.environ.get("ATTENDANCE_LIST_USER"),
        host=os.environ.get("ATTENDANCE_LIST_HOST"),
        password=os.environ.get("ATTENDANCE_LIST_PASSWORD")
    ))
    conn.autocommit = True
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def disconnect():
    cur.close()
    conn.close()


def select():
    cur.execute('''
    SELECT id, name, ROW_NUMBER () OVER (ORDER BY id) FROM attendance;
    ''')
    present_pylighters = cur.fetchall()
    return present_pylighters


def insert(pylighter_input):
    cur.execute('''
    INSERT INTO attendance (name) VALUES (%s);
    ''', (pylighter_input,))


def delete(pylighter_input):
    cur.execute('''
    DELETE FROM attendance
    WHERE id = %s;
    ''', (pylighter_input,))


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
