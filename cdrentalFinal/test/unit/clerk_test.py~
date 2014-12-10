import unittest
from customer import *
from customers import *
from cds import *
from cd import *
from clerk import *

class TestClerk(unittest.TestCase):

	def test_clerk_can_get_Customer_data_from_dictionary(self):
		cds = Cds()
		cd_1 = Cd("00-01","3 Idiots", "false","none") 
		cds.add_cd(cd_1) 
		customer_1 = Customer("000-001","jack", 0, [])
		customers = Customers()
		customers.add_customer(customer_1) 
		self.assertEqual(customers.get_customer_name("000-001"), "jack")
		self.assertEqual(customers.get_customer_rentedArray("000-001"), [])
		self.assertEqual(customers.get_customer_rented("000-001"), 0)

	def test_clerk_can_get_Cd_data_from_dictionary(self):
		cds = Cds()
		cd_1 = Cd("00-01","3 Idiots", "false","none") 
		cds.add_cd(cd_1) 
		customer_1 = Customer("000-001","jack", 0, [])
		customers = Customers()
		customers.add_customer(customer_1) 
		self.assertEqual(customers.get_customer_name("000-001"), "jack")
		self.assertEqual(customers.get_customer_rentedArray("000-001"), [])
		self.assertEqual(customers.get_customer_rented("000-001"), 0)

	def test_clerk_can_checkout(self):
		cds = Cds()
		cd_1 = Cd("00-01","3 Idiots", "false","none") 
		cds.add_cd(cd_1) 
		customer_1 = Customer("000-001","jack", 0, [])
		customers = Customers()
		customers.add_customer(customer_1)
		clerk = Clerk(customers, cds) 
		clerk.checkout("000-001", "00-01")
		self.assertEqual(customers.get_customer_name("000-001"), "jack")
		self.assertEqual(customers.get_customer_rentedArray("000-001"), ["3 Idiots"])
		self.assertEqual(customers.get_customer_rented("000-001"), 1)
		self.assertEqual(cds.get_cd_rentedBy("00-01"), "jack")

		def test_clerk_can_checkout_many_cds(self):
			cds = Cds()
			cd_1 = Cd("00-01","3 Idiots1", "false","none") 
			cds.add_cd(cd_1)
			cd_2 = Cd("00-01","3 Idiots2", "false","none") 
			cds.add_cd(cd_2) 
			cd_3 = Cd("00-01","3 Idiots3", "false","none") 
			cds.add_cd(cd_3) 

			customer_1 = Customer("000-001","jack", 0, [])
			customers = Customers()
			customers.add_customer(customer_1)

			clerk = Clerk(customers, cds) 
			clerk.checkout("000-001", "00-01")
			clerk.checkout("000-001", "00-02")
			clerk.checkout("000-001", "00-03")

			self.assertEqual(customers.get_customer_name("000-001"), "jack")
			self.assertEqual(customers.get_customer_rentedArray("000-001"), \
										 ["3 Idiots1","3 Idiots2","3 Idiots3"])

			self.assertEqual(customers.get_customer_rented("000-001"), 3)
			self.assertEqual(cds.get_cd_rentedBy("00-01"), "jack")
			self.assertEqual(cds.get_cd_rentedBy("00-02"), "jack")
			self.assertEqual(cds.get_cd_rentedBy("00-03"), "jack")

 			cd_4 = Cd("00-01","3 Idiots3", "false","none") 
			cds.add_cd(cd_4) 
			self.assertEqual(clerk.checkout("000-001", "00-03"), "exceeded")