#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 08:49:42 2017

@author: Gipfeli
"""

from bs4 import BeautifulSoup 
import requests
import psycopg2

# XML-Flie should be in same folder like py-File
def getdatafromlocal():
    BeautifulSoup(open("ch.ofac.ca.covercard.CaValidationHorizontale.xml", "r", encoding="windows-1252"),"lxml")
    return;

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

###############################################################################

soup = getdatafromURL()

data = {
   "KK-Nummer": soup.client.attrs['assure-id'],
   "AHV-Nummer": soup.client.attrs['cardholderidentifier'],
   "Vorname": soup.find(name='first-name').string,
   "Nachname": soup.find(name='last-name').string,
   "Geburtstag": soup.find(name='birth-date').string,
   "Adresse": soup.find(name='street').string,
   "PLZ": soup.find(name="zip").string
        }

sql =   """
        INSERT INTO test080317.testdb (first,last,kkv) 
        VALUES (%s,%s,%s) RETURNING test080317.testdb.id
        """
data = getdatafromURL()

# Connect to database using config function above
# TODO: use configparser to put login info in separated file
conn = psycopg2.connect(host="localhost", port=5432, dbname='Gipfeli', user='Gipfeli', password='')
print('Connected to database')
# Create a cursor
cur = conn.cursor()
# Insert the data into table: patient
# and request the patient_id
id = cur.execute(sql, (data['Nachname'],data['Vorname'],data['KK-Nummer']))
# commit the changes to the database
conn.commit()