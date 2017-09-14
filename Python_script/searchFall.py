# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 01:59:29 2017

@author: Gipfeli
"""

from config import connection

import psycopg2

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def search(key):
    conn = None
    try:
        params = connection()

        logger.debug('Connect to the Postgresql database....')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        sql = searchOpenCase()
        cur. execute(sql,(key))
        
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
            
def searchOpenCase():
    sql_opening = """
               SELECT kf.fall_id, kf.betreff, kf.ist_krankheit
               FROM konsultation.fall AS kf
               WHERE kf.patient_id = %s AND kf.fll_geschlossen = FALSE;
              """
    return sql_opening;

###############################################################################

if __name__ == '__main__':

    key = input('Patient ID: ')
    
    search(key)