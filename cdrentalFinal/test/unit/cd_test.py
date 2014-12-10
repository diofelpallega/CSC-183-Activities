
import unittest
from cd.cd import *

class TestCustomer(unittest.TestCase):
    def test_if_customer_account_can_be_created(self):
        cd = Cd("01","hlo","false","jack")
        self.assertEqual(cd.cd_id, "01")
        self.assertEqual(cd.title, "hlo")
        self.assertEqual(cd.isrented, "false")
        self.assertEqual(cd.rentedBy,"jack")



if __name__ == '__maine__':
    unittest.main()
