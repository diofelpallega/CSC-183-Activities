from cd.dosql import *
import cgi
import psycopg2
import sys
try:
    import json
except ImportError:
    import simplejson as json


con = None

try:
     
    con = psycopg2.connect("dbname='cdrental' user='postgres' password='password' host='127.0.0.1' port='5433'")   
    
    cur = con.cursor()
 
    cur.execute("SELECT update_customer(CAST ('aliana' AS text) ,0,CAST ('[]' AS text))")  
    con.commit()

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()




