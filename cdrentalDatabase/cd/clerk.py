from dosql import *

class Clerk(object):
    def __init__(self):
        pass
    def checkout(self,cdid,customerid):
        
        b = doSql()

        query = "SELECT get_customer_rented('"+customerid +"' );" 
        items =  b.execqry(query,False)             
 	result = []	
        for item in items:
            stringed = map(str, item)
            result.append(stringed)
	[[new]]  = result
	return new    
