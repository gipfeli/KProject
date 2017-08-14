#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 02:34:27 2017

@author: Gipfeli
"""
from datetime import datetime

# This flie allow create, edit or delete patient info out of the DB

def action():
    def getChoice():
        var = input("Press 1 to add a new patient, 2 to edit and 3 to delete data: ")
        return var;
    
    choice = getChoice()
    print(choice)

# Prepare SQL INSERT for table, Patient
def insertpatient():
    
    sql =   """
            INSERT INTO patient (vorname,nachname,geschlecht,geburtstag,adresse_id,kk_nummer,ahv_nummer) 
            VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING patient_id
            """
    return sql;

# Sex
def f(x):
    return {
        'm': 1,
        'w': 2
    }.get(x, 9) 

# Manual enter data (not through HIN) => Use xmlparser.py for auto insert.
def addPatient():
    data = {
       "KK-Nummer": input('KK Nummer: '),
       "AHV-Nummer": input('AHV Nummer: '),
       "Vorname": input('Vorname: '),
       "Nachname": input('Nachname: '),
       "Geschlecht": f(input('m = männlich, w = weiblich: ')),
       "Geburtstag": datetime.strptime(input('Geburtstag (DD-MM-YYYY): '), '%d-%m-%Y'),
       "Adresse": input('Adresse: '),
       "PLZ": input('PLZ: ')
       }
    return data;

new = addPatient()