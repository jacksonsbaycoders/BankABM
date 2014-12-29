debug = False
import institutions
class Person:
	count = 0
	
	def __init__(self,bank):
		if debug :print "initilised"
		self.id = Person.count
		Person.count +=1
		self.bank = bank
		self.bank.add_client(self.id)
	
	def to_string(self):
		s = str(self.id)
		s = s+self.bank.name
		return s

