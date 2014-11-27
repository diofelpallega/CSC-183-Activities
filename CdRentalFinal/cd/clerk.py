from customer import *
from cd import *
from customers import *
from cds import *

class Clerk(object):

	def __init__(self, customers, cds): 
		self.customers = customers
		self.cds = cds


	def checkout(self, customer_id, cd_id):
		customers = self.customers  
		cds = self.cds

		 
		if(type(customer_id) == str and type(cd_id) == str):
			if((customers.get_customer_rented(customer_id) <= 3)):

				if ((customer_id in customers.dictionary) and \
					(customers.get_customer_rented(customer_id) <= 3)) :

					customers.update_add_customer_rented(customer_id)
					cds.dictionary[cd_id][2] = customers.dictionary[customer_id][0] 
					Array = customers.dictionary[customer_id][2] 
					customers.dictionary[customer_id][2] = Array + [cds.get_cd_title(cd_id)]
	
				else:
					print "Id does not exist"

			else:
				print "You have exceeded your renting limit" 
				return "exceeded"
		else:
			print "invalid input"