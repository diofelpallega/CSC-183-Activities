import unittest
from cd import *
from cds import *

class CdsTest(unittest.TestCase):
	def test_cds_is_initially_empty(self):
		cds = Cds()
		self.assertEqual({}, cds.dictionary)
		self.assertEqual(len(cds.dictionary), 0)

	def test_add_cd(self):
		cds = Cds()
		cd_1 = Cd("01","3 Idiots", "false", "none") 
		cd_2 = Cd("02","Edge of Tomorrow","false","none")
		cds.add_cd(cd_1)
		cds.add_cd(cd_2)
		self.assertEqual(len(cds.dictionary), 2)

	def test_get_cd_info(self):
		cds = Cds()
		cd_1 = Cd("01","3 Idiots", "false", "none")
		cds.add_cd(cd_1)
		self.assertEqual(cds.get_cd_title("01"), "3 Idiots")
		self.assertEqual(cds.get_cd_isrented("01"), "false") 
		self.assertEqual(cds.get_cd_rentedBy("01"), "none") 

if __name__ == '__main__':
	unittest.main()