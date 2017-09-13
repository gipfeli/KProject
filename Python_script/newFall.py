#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 02:30:30 2017

@author: Gipfeli
"""
from config import connection
import searchPatient

import psycopg2

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Choose patient, who'd receive the consultation:
def getPatientID():
    var = input("Patient ID: ")
    return var;

# List all cases of a patient:
def connect():
    conn = None
    try:
        params = connection()

        logger.debug('Connect to the Postgresql database....')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        option = 1 # Temp. placeholder
        
        if option == 1:
            sql1 = sqlgetLastID()
            logger.debug(sql1)
            sql2 = sqlnew()
            logger.debug(sql2)
            
            cur.execute(sql1) #Get the last ID in Addressbook
            fall_id = cur.fetchone()[0] + 1
            print('New case ID: %s', fall_id)
            betreff = input('Betreff: ')
            patient_id = varID
            cur.execute(sql2,(betreff, patient_id))
        else:
            print('Other options are under construction')
            pass

        conn.commit()
        
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        if conn is not None:
            conn.close()
            logger.debug('Database connection closed.')
            
###############################################################################

def sqlgetLastID():
    sql_lastID = """
                 SELECT COALESCE((SELECT fall_id FROM konsultation.fall ORDER BY fall_id DESC LIMIT 1),0);
                 """
    return sql_lastID;

def sqlnew():
    sql_newCase = """
                  INSERT INTO konsultation.fall (betreff, patient_id)
                  VALUES (%s,%s);
                  """
    return sql_newCase;
    
## ToDO: Edit and delete cases.

###############################################################################

if __name__ == '__main__':

    key = input('Search patient: ')
    var = '%' + key + '%'
    
    searchPatient.connect(key,var)
    print("Enter the ID of the patient: ")
    varID = getPatientID()
    
#    option = input("Press 1 to add new, 2 to edit and 3 to delete a case: ")
    connect()
    
    
    