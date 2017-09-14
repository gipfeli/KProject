# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:08:50 2017

@author: Gipfeli
"""

#from config import connection
import searchPatient
import newFall

#import psycopg2

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


###############################################################################

if __name__ == '__main__':

    key = input('Search keywords: ')
    var = '%' + key + '%'
    
    searchPatient.search(key,var)
    print("Enter the ID of the patient: ")
