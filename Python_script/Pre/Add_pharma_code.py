# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Library to read/convert Excel to CSV file.
from xlrd import open_workbook
import csv

# Library to connect to server
from config import connection
import psycopg2

dataname="../ReferenzenDB/Pharmacode.xls"

# Convert the file (Only need to run once, as there won't be any new Pharmacode after 1.1.2015)
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
def insertPharmaCode():
    sql =   """
        UPDATE "referenzen"."tbl_medlist"
        SET "pharmacode" = %s
        WHERE "swissmedic_nr" = %s;
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
        
        for row in readdata:
            pharmacode = row[2][0:7]
            swissmedic_nr = row[4][0:8]
            cur.execute(sql,(pharmacode,swissmedic_nr))

        conn.commit()
        
        cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            


###############################################################################

if __name__ == '__main__':
    
    convertData()
    readdata = csv.reader(open('../ReferenzenDB/Publications.csv'))
    sql = insertPharmaCode()
    connect()