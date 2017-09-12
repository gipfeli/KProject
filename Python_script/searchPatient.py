# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 02:55:46 2017

@author: Gipfeli
"""

from config import connection

import psycopg2

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def connect(key,var):
    conn = None
    try:
        params = connection()

        logger.debug('Connect to the Postgresql database....')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        if key.isdecimal():
            sql = searchforKK()
            logger.debug(sql)
            cur.execute(sql, (var,))
        else:
            sql = searchforName()
            logger.debug(sql)
            cur.execute(sql, (var, var))
        
#        logger.info(cur.fetchall())
        
        row = cur.fetchone()
        print(row)
        while row:
            row = cur.fetchone()
            print(row)
            
        conn.commit()
        
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        if conn is not None:
            conn.close()
            logger.debug('Database connection closed.')
            
def searchforName():
    sql_name = """
              SELECT patient_id, vorname || ' ' || nachname AS fullname, kk_nummer
              FROM patient
              WHERE vorname ILIKE (%s) OR nachname ILIKE (%s)
              LIMIT 25;
              """
    return sql_name;

def searchforKK():
    sql_nummer = """
              SELECT patient_id, vorname || ' ' || nachname AS fullname, kk_nummer
              FROM patient
              WHERE kk_nummer ILIKE (%s)
              LIMIT 25;
              """
    return sql_nummer;
                
            
###############################################################################

if __name__ == '__main__':

    key = input('Search keywords: ')
    var = '%' + key + '%'
    
    connect(key,var)


      