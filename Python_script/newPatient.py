#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 08:49:42 2017

@author: Gipfeli
"""
from config import connection

from bs4 import BeautifulSoup 
import requests
import psycopg2

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# XML-Flie should be in same folder like py-File
def getdatafromlocal():
    soup = BeautifulSoup(open("ch.ofac.ca.covercard.CaValidationHorizontale.xml", "r", encoding="windows-1252"),"lxml")
    return soup;

# Get XML file directly from URL: http://blabla.com/asd=xxxxxxxxx, where xxxxxxxxx is KK-Nr (get though input or a given list)
def getdatafromURL():
    def getKKnr():
        var = input("KK Nummer hier: ")
        return var;

    var = getKKnr()    
    url = "http://covercard.hin.ch/covercard/servlet/ch.ofac.ca.covercard.CaValidationHorizontale?type=XML&langue=1&carte=" + var + "&ReturnType=STPLUS"
    content = requests.get(url)
    soup = BeautifulSoup(content.text,"lxml")

    return soup;

# Prepare data
def preparedata():
    soup = getdatafromURL()
    data = {
       "KK-Nummer": soup.client.attrs['insuredpersonnumber'],
       "AHV-Nummer": soup.client.attrs['cardholderidentifier'],
       "Vorname": soup.find(name='first-name').string,
       "Nachname": soup.find(name='last-name').string,
       "Geschlecht": soup.find("ns1:entity").attrs['sex'],
       "Geburtstag": soup.find(name='birth-date').string,
       "Adresse": soup.find(name='street').string,
       "PLZ": soup.find(name="zip").string
       }
    return data;
    
# Prepare SQL INSERT for table, Patient
def insertpatient():
    
    sql =   """
            INSERT INTO patient (vorname,nachname,geschlecht,geburtstag,adresse_id,kk_nummer,ahv_nummer) 
            VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING patient_id;
            """
    return sql;

# Prepare SQL INSERT for table, Adressenbuch
def insertaddress():
    
    sql =   """
            INSERT INTO adressebuch (adresse_id, adresse, plz) 
            VALUES (%s,%s,%s);
            """
    return sql;

# Commit the data into database
def addnew():
    conn = None
    try:
        params = connection()

        
        logger.info('Connect to the Postgresql database....')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        
        logger.info('PostgreSQL database Version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        logger.info(db_version)
        
        cur.execute("SELECT adresse_id FROM adressebuch ORDER BY adresse_id DESC LIMIT 1;") #Get the last ID in Addressbook
        adresse_id = cur.fetchone()[0] + 1
        
        cur.execute(sql1, (adresse_id, data['Adresse'], data['PLZ']))
        
        cur.execute(sql2, (data['Vorname'],data['Nachname'],data['Geschlecht'], 
                           data['Geburtstag'],adresse_id, data['KK-Nummer'], data['AHV-Nummer']))
        patient_id = cur.fetchone()
        conn.commit()
        
        logger.debug('Patient ID: ', patient_id)
        
        logger.debug('Adresse ID: ', adresse_id)
        
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

###############################################################################

if __name__ == '__main__':
    
    data = preparedata()
    logger.debug(data)
    
    sql1 = insertaddress()
    logger.debug('SQL Address: ', sql1)
    sql2 = insertpatient()
    logger.debug('SQL Patient info: ', sql2)

    addnew()