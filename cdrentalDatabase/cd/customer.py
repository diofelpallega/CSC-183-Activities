from dosql import *

class Customer(object):
    def __init__(self,rentalid,name,rented):
        self.name = name
	self.rentalid = rentalid
	self.rented = rented

    def addcustomer(self):
        b = doSql()

        query = "SELECT add_customer('"+self.rentalid +"','"+self.name+"' );" 
        items =  b.execqry(query,True)             
 	result = []	
        for item in items:
            stringed = map(str, item)
            result.append(stringed)
	[[new]]  = result
	return new        
