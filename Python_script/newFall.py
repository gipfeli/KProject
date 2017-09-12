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
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Choose patient, who'd receive the consultation:
def getPatientID():
    var = input("Patient ID: ")
    return var;

###############################################################################

if __name__ == '__main__':

    key = input('Search patient: ')
    var = '%' + key + '%'
    
    searchPatient.connect(key,var)
    print("Enter the ID of the patient: ")
    var = getPatientID()
    

    
    
    