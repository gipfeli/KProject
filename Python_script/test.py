# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 00:45:05 2017

@author: Dat
"""

from config import connection

import psycopg2

def connect():
    conn = None
    try:
        params = connection()

        print('Connection to the Postgresql database....')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print('PostgreSQL database Version:')
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