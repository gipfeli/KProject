#!//usr/local/bin/python 
# -*- coding: utf-8 -*-

import psycopg2
import time

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as cv

conn = psycopg2.connect(host="localhost", port=5432, dbname='Gipfeli', user='Gipfeli', password='')
print('Connected to database')
cur = conn.cursor() #Create the cursor

cur.execute(
"""
SELECT p.nachname, p.vorname, ps.ahv_nr, ps.birthday, ci.address, ci.plz, plz.ortsname
FROM test080317.patient AS p
  INNER JOIN test080317.current_health AS d ON p.patient_id = d.patient_id
  INNER JOIN test080317.personalien AS ps ON p.patient_id = ps.patient_id
  INNER JOIN test080317.contact_info AS ci ON p.patient_id = ci.patient_id
  INNER JOIN test080317."db.plz" AS plz ON ci.plz = plz.plz
  WHERE p.patient_id = 1;"""
)
row1 = cur.fetchone()
 
cv = cv.Canvas('myfile.pdf', pagesize=A4)
width, height = A4

cv.setLineWidth(.3)
cv.setFont('Helvetica', 30)
 
cv.drawString(30,750,'Stark Industries')

cv.setFont('Helvetica', 12)
cv.drawString(500,750,time.strftime("%d/%m/%Y"))
cv.line(480,747,580,747)

full_name = row1[0] + ' ' + row1[1]

cv.drawString(30,730,'Name: ' + full_name)
cv.drawString(30,715,'Adresse: ' + row1[4])
cv.drawString(80,700,row1[5] + ' ' + row1[6])

cv.drawString(450, 730, 'AHV: ' + row1[2])
cv.drawString(450,715,'Geburtstag: ' + row1[3].strftime('%d, %b %Y'))

cv.showPage()
cv.save()