import psycopg2
import psycopg2.extras
import yaml
import os


# Connect to the database
def connect():
    config = {}
    yml_path = os.path.join(os.path.dirname(__file__), '../config/db.yml')
    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])


# Perform the specified file from the path
def exec_sql_file(path):
    full_path = os.path.join(os.path.dirname(__file__), f'../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()

# Return data in a tuple (ONLY USED FOR QUERIES)


def exec_get_one(sql, args):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

# Return data in a dictionary (ONLY USED FOR QUERIES)


def exec_get_one_as_dict(sql, args):
    conn = connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

# Return data in a list of tuples (ONLY USED FOR QUERIES)


def exec_get_all(sql, args):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples

# Return the result of commit (DOES NOT WORK WITH RETURNING STATEMENT)


def exec_commit(sql, args):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result

# Return the result of commit INCLUDING RETURNING STATEMENTS


def exec_commit_returning(sql, args):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    postgresql_returning = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return postgresql_returning
