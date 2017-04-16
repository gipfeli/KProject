#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:15:15 2017

@author: Gipfeli
"""

from config import connection

import psycopg2

# Commit the data into database
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
            
            
csv = open('versicher.csv', 'r')
