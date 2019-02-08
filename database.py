import os
import psycopg2
import psycopg2.extras


def database_handler(func):
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect("dbname={dbname} user={user} password={password} host={host}".format(
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            host=os.environ.get("HOST"),
            password=os.environ.get("PASSWORD")
        ))
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        wrapped_func = func(cur, *args, **kwargs)
        conn.commit()
        cur.close()
        conn.close()
        return wrapped_func
    return wrapper


@database_handler
def insert(cur, pylighter_input):
    cur.execute('''
    INSERT INTO attendance (name) VALUES (%s);
    ''', (pylighter_input,))


@database_handler
def delete(cur, pylighter_input):
    cur.execute('''
    DELETE FROM attendance
    WHERE id = %s;
    ''', (pylighter_input,))


@database_handler
def select(cur):
    cur.execute('''
    SELECT id, name, ROW_NUMBER () OVER (ORDER BY id) FROM attendance;
    ''')
    present_pylighters = cur.fetchall()
    return present_pylighters


@database_handler
def create_table(cur):
    cur.execute('''
    CREATE TABLE attendance (
        id serial PRIMARY KEY,
        name TEXT
    );
    ''')


@database_handler
def drop_table(cur):
    cur.execute('''
    DROP TABLE attendance;
    ''')
