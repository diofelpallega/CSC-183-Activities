import unittest
from cd.customer import *
from cd.cd import *
from cd.dosql import *
from cd.clerk import *

class TestClerk(unittest.TestCase):

	def test_clerk_can_add_cd(self):
	    cd = Cd('Edge of Tomorrow','False','none')
	    result = cd.updatecd()
	        
	    self.assertEqual(result, 'OK')

	def test_clerk_can_add_customer(self):
	    customer = Customer('1','person','none')
	    result = customer.addcustomer()
	    self.assertEqual(result, 'Already added in the system')

	def test_clerk_can_checkout(self):
 	    clerk = Clerk()
	    result = clerk.checkout('1','1')
	    self.assertEqual(result, 'Ok')	 
