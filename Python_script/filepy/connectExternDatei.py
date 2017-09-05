import psycopg2
from connecter import verbindung   #connecter ist file name (connecter.py)

def connect():
    conn = None
    try:
        params = verbindung()

        print('Connection to the Postgresql database....')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print('PostgreSQL databaser Version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()