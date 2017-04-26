import sys
import PyQt5.QtWidgets as widgets
import PyQt5.uic as uic
import PyQt5.QtGui as gui
import PyQt5.QtCore as core

from bs4 import BeautifulSoup
import requests
import psycopg2

import datetime

from PyQt5.QtWidgets import (QMdiArea)

app = widgets.QApplication(sys.argv)
w = uic.loadUi("start100.ui")
covercard = uic.loadUi("covercard.ui")
#mdi = uic.loadUi("mdiTest.ui")

def getdatafromURL():
    def getKKnr():
        var = input("KK Nummer hier: ")
        return var;

    var = getKKnr()
    url = "http://covercard.hin.ch/covercard/servlet/ch.ofac.ca.covercard.CaValidationHorizontale?type=XML&langue=1&carte=" + var + "&ReturnType=STPLUS"
    content = requests.get(url)
    soup = BeautifulSoup(content.text,"lxml")

    return soup;


def ClickCovercard():
    def getdatafromURL():
        covercardnummer = covercard.lineEditCovercardEingabe.text()
        url = "http://covercard.hin.ch/covercard/servlet/ch.ofac.ca.covercard.CaValidationHorizontale?type=XML&langue=1&carte=" + covercardnummer + "&ReturnType=STPLUS"
        content = requests.get(url)
        soup = BeautifulSoup(content.text, "lxml")
        return soup;

    soup = getdatafromURL()
    print("Data richtig gelesen")

    data = {
        "KK-Nummer": soup.client.attrs['insuredpersonnumber'],
        "AHV-Nummer": soup.client.attrs['cardholderidentifier'],
        "Vorname": soup.find(name='first-name').string,
        "Nachname": soup.find(name='last-name').string,
        "Geburtstag": soup.find(name='birth-date').string,
        "Adresse": soup.find(name='street').string,
        "PLZ": soup.find(name="zip").string,
        "Ort": soup.find(name="city").string

    }

    covercard.lineEditNachname.setText(soup.find(name='last-name').string)
    covercard.lineEditVorname.setText(soup.find(name='first-name').string)
    covercard.lineEditAHV.setText(soup.client.attrs['cardholderidentifier'])
    covercard.lineEditCovercardNr.setText(soup.client.attrs['insuredpersonnumber'])
    geb = soup.find(name='birth-date').string
    gebConvert=datetime.datetime.strptime(geb,'%Y-%m-%d').strftime('%d.%m.%Y')
    #w.lineEditGeb.setText(soup.find(name='birth-date').string)
    covercard.lineEditGeb.setText(gebConvert)
    covercard.lineEditStrasse.setText(soup.find(name='street').string)
    covercard.lineEditPlz.setText(soup.find(name='zip').string)
    covercard.lineEditOrt.setText(soup.find(name='city').string)
    testNachname = covercard.lineEditNachname.setText(soup.find(name='last-name').string)
    print(data)
    print(data['Nachname'])




def DiaglocCovercard():
    covercard.show()

def ClickSpeichern(self):

    print("speichern")
   # ClickCovercard()
    nachname = covercard.lineEditNachname.text()
    vorname = covercard.lineEditVorname.text()
    KK = covercard.lineEditCovercardNr.text()
    sql = """
            INSERT INTO test080317.patient (nachname,vorname,"KK_nummer") 
            VALUES (%s,%s,%s) RETURNING test080317.patient."patient_id"
            """
    print(sql)

    #print(data)

    # Connect to database using config function above
    # TODO: use configparser to put login info in separated file
    conn = psycopg2.connect(host="localhost", port=5432, dbname='mm-khanh', user='mm-khanh', password='')
    print('Connected to database')
    # Create a cursor
    cur = conn.cursor()
    # Insert the data into table: patient
    # and request the patient_id
    #id = cur.execute(sql, (data['Nachname'], data['Vorname'], data['KK-Nummer']))
    id = cur.execute(sql, (nachname, vorname,KK))
    # commit the changes to the database
    conn.commit()



covercard.pushButtonXmlLesen.clicked.connect(ClickCovercard)
w.actionCovercard.triggered.connect(DiaglocCovercard)

covercard.pushButtonSpeichern.clicked.connect(ClickSpeichern)

w.show()


sys.exit(app.exec_())