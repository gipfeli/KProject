import psycopg2
from config import config

#conn_string = "dbname='praxisDB' user='mm-khanh' host='localhost' password='' port='5432'"
#print("Connection to database\n ->%s" % (conn_string))

#conn = psycopg2.connect(conn_string)
#cur  = conn.cursor()

#cur.execute("CREATE TABLE tblPatient("
#            "paId int NOT NULL,"
#            "paName character varying (35),"
#            "paVorname character varying (35),"
#            "PRIMARY KEY(paID) )")
#cur.execute("insert into tblpatient values ((select max(paId)+1 from tblpatient),'Neu','Hans','bahn 1')")
#cur.execute("insert into tblbehandlung values (1,'2017-03-25','kopfweh')")


#create_table()

def insert_patient(patnachname,patvorname):
    sql1 = """insert into patient(patnachname,patvorname) 
                values (%s,%s) returning patid;"""
    #sql2 = "insert into tblpatient(panachname) values (%s)"
    conn = None
    patid = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql1,(patnachname,patvorname,))
        patid = cur.fetchone()[0]
        conn.commit()
        cur.close()       
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return patid
if __name__ == '__main__':
    nname = input('nachname: ')
    vname = input ('vorname: ')
    insert_patient(nname,vname)
 
    
    
#query = "INSERT INTO tblPatient (paId,paName,paVorname,paStrasse) VALUES (%s,%s,%s,%s);"
#data = (1,"Mustermann","Hans","teststrasse 2")


#cur.execute(query,data)
#conn.commit()

#cur.execute(""" Insert into tblpatient(paId) values (1) """)
#conn.commit()
