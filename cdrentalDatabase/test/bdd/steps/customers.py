from customer import *

class Customers(object):
	def __init__(self):
		self.dictionary = {}

	def add_customer(Customers, customer):
		Customers.dictionary[customer.customer_id] = [customer.name,  \
												 customer.rented,\
												 customer.rentedArray]
		print Customers.dictionary

	def get_customer_name(Customers, customer_id): 
		return Customers.dictionary[customer_id][0]


	def get_customer_rented(Customers, customer_id): 
		return Customers.dictionary[customer_id][1]
	 
	 


	def get_customer_rentedArray(Customers, customer_id):
		return Customers.dictionary[customer_id][2]
		 

	def update_add_customer_rented(Customers,customer_id):
		Customers.dictionary[customer_id][1] += 1
		 
 
 