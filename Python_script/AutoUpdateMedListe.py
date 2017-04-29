#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 01:24:36 2017

@author: Gipfeli
"""
# Library to retrieve the file
import urllib.request
from urllib.error import URLError, HTTPError

# Library to convert Excel to CSV file.
from xlrd import open_workbook
import csv

# Library to remove old data
from os import remove

# Retrieve the file.
req = "http://www.listedesspecialites.ch/File.axd?file=Publications.xls"
dataname = "updatedb.xls"
try:
    response = urllib.request.urlretrieve(req,dataname)
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
wb = open_workbook(dataname)
 
i = 0 # Sheet needed to update, array index!
sheet = wb.sheet_by_index(i)
print(sheet.name)
with open("ReferenzenDB/%s.csv" %(sheet.name.replace(" ","")), "w") as file:
    writer = csv.writer(file, delimiter = ",")
    print(sheet, sheet.name, sheet.ncols, sheet.nrows)
 
    header = [cell.value for cell in sheet.row(0)]
    writer.writerow(header)
 
    for row_idx in range(1, sheet.nrows):
        row = [int(cell.value) if isinstance(cell.value, float) else cell.value
               for cell in sheet.row(row_idx)]
        writer.writerow(row)
        
# Clean up the old excel file
tidy = remove(dataname)
print('All done')
