#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 01:24:36 2017

@author: Gipfeli
"""
# Library to retrieve the file
import urllib.request
from urllib.error import URLError, HTTPError

# Library to read/convert Excel to CSV file.
from xlrd import open_workbook
import csv

# Library to remove old data
from os import remove

# Library to connect to server
from config import connection
import psycopg2

# Library to correctly convert date to ISO 8601
import datetime
############################################

dataname = "updatedb.xls"

# Commit the data into database
def connect():
    conn = None
    try:
        params = connection()

        print('Connection to the Postgresql database....')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(cleartb)
        
        for row in readdata:
            seconds = (float(row[6]) - 25569.0) * 86400.0
            date = datetime.datetime.utcfromtimestamp(seconds).date()
            swissmedic_nr = row[4][0:8]
            gtin = row[16][0:13]
            cur.execute(sql,(row[7],date,swissmedic_nr,gtin,row[9]))

        conn.commit()
        
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

############################################

# Retrieve the file.
def retrieveData():
    req = "http://www.listedesspecialites.ch/File.axd?file=Publications.xls"
    try:
        urllib.request.urlretrieve(req,dataname)
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
    except URLError as e:
        # do something
        print('Reason: ', e.reason)
    else:
        # do something
        print('Done!')
        
# Convert the file
def convertData():
    wb = open_workbook(dataname)
     
    i = 0 # Sheet needed to update, array index!
    sheet = wb.sheet_by_index(i)
    print(sheet.name)
    with open("../ReferenzenDB/%s.csv" %(sheet.name.replace(" ","")), "w") as file:
        writer = csv.writer(file, delimiter = ",")
        print(sheet, sheet.name, sheet.ncols, sheet.nrows)
     
#        header = [cell.value for cell in sheet.row(0)]                     # Remove if need header
#        writer.writerow(header)
     
        for row_idx in range(1, sheet.nrows):                               
            row = [int(cell.value) if isinstance(cell.value, int)           # If the row is int => int, or float => float, or else, string
                else float(cell.value) if isinstance(cell.value, float)     # The easiest way, is simply call cell.value, and get everything in float.
                else cell.value
                   for cell in sheet.row(row_idx)]
            writer.writerow(row)

# Prepare the INSERT - SQL command
def insertMed():
    sql =   """
        INSERT INTO "referenzen"."tbl_medlist"("bezeichnung", "einf_datum", "swissmedic_nr", "gtin", "preis") 
        VALUES(%s,%s,%s,%s,%s)
        """
    return sql;

# Truncate, also clear table, before updating
def clearTbl():
    sql =   """
        TRUNCATE TABLE "referenzen"."tbl_medlist"
        RESTART IDENTITY
        CASCADE;
        """
    return sql;

# Clean up the old excel file
def tidyup():
    remove(dataname)


###############################################################################

if __name__ == '__main__':
    
    retrieveData()
    convertData()
    readdata = csv.reader(open('../ReferenzenDB/Publications.csv'))
    cleartb = clearTbl()
    sql = insertMed()
    connect()
    tidyup()
