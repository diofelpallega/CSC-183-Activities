from dosql import *


class Cd(object):
    def __init__(self, title, isrented, rentedby):
        self.title = title
        self.isrented = isrented
	self.rentedby = rentedby 
    def updatecd(self):
        b = doSql()
        query = "SELECT update_cd('"+self.title +"','"+self.isrented+"','"+self.rentedby+"');" 
        items =  b.execqry(query,True)             
        result = []	
        for item in items:
            stringed = map(str, item)
            result.append(stringed)
        [[new]]  = result 
	return new
