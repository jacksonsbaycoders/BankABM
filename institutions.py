debug = False
class Bank:
	def __init__(self,name):
		if debug : print "init"
		self.name = name
		self.clients = {}

	def add_client(self, id):
		ac_id = "id"+str(id)
		if debug : print "id:",id
		self.clients[ac_id]=0

	def list_clients(self):
		s=""
		for c in self.clients:
			s+=c+","+str(self.clients[c])+","
		return s

if __name__ == '__main__':
	debug = True
	tb = Bank()
	tb.add_client('0')
	for s in tb.clients:
		print "id:",s,"account",tb.clients[s]
