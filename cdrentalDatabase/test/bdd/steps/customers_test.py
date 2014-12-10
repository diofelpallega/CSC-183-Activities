import unittest
from customer import Customer
from customers import Customers


class CustomersTest(unittest.TestCase):
	def test_customers_is_initially_empty(self):
		customers = Customers()
		self.assertEqual({}, customers.dictionary)
		self.assertEqual(len(customers.dictionary), 0)

	def test_add_customer(self):
		customers = Customers()
		customer_1 = Customer("001","jack", 0, []) 
		customer_2 = Customer("002","jack2", 0, [])
		customers.add_customer(customer_1)
		customers.add_customer(customer_2)
		self.assertEqual(len(customers.dictionary), 2)

	def test_get_customer_info(self):
		customers = Customers()
		customer_1 = Customer("001","jack", 0, [])
		customers.add_customer(customer_1)
		self.assertEqual(customers.dictionary, {'001': ['jack', 0, []]})
		self.assertEqual(customers.get_customer_rented("001"), 0)
		self.assertEqual(customers.get_customer_rentedArray("001"), [])

if __name__ == '__main__':
	unittest.main()