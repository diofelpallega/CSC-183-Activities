from cd import *

class Cds(object):
	def __init__(self):
		self.dictionary = {}

	def add_cd(Cds, cd):
		Cds.dictionary[cd.cd_id] = [cd.title, cd.isrented, cd.rentedBy]

	def get_cd_title(Cds, cd_id):
		return Cds.dictionary[cd_id][0]


	def get_cd_isrented(Cds, cd_id):
		return Cds.dictionary[cd_id][1]

	def get_cd_rentedBy(Cds, cd_id):
		return Cds.dictionary[cd_id][2]

 