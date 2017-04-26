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
            VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING patient_id
            """
    return sql;

# Prepare SQL INSERT for table, Adressenbuch
def insertaddress():
    
    sql =   """
            INSERT INTO adressebuch (adresse, plz) 
            VALUES (%s,%s) RETURNING adresse_id
            """
    return sql;

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
        
        cur.execute(sql1, (data['Adresse'], data['PLZ']))
        adresse_id = cur.fetchone()
        
        cur.execute(sql2, (data['Vorname'],data['Nachname'],data['Geschlecht'], 
                               data['Geburtstag'],adresse_id, data['KK-Nummer'], data['AHV-Nummer']))
        patient_id = cur.fetchone()
        conn.commit()
        
        print('Patient ID: ', patient_id)
        
        print('Adresse ID: ', adresse_id)
        
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
    print(data)
    
    sql1 = insertaddress()
    sql2 = insertpatient()
    print(sql2)
    
    connect()