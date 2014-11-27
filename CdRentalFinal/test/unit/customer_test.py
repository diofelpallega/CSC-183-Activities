import unittest
from customer import *

class TestCustomer(unittest.TestCase):
    def test_if_customer_account_can_be_created(self):
        customer = Customer("001","Jack", 0, [])
        self.assertEqual(customer.customer_id, "001")
        self.assertEqual(customer.name, "Jack")
        self.assertEqual(customer.rented, 0)
        self.assertEqual(customer.rentedArray,[])



if __name__ == '__maine__':
    unittest.main()