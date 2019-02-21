from pyignite import Client

class Database:
	def __init__(self, url='127.0.0.1', port=10800) :
		self.client = Client()
		self.client.connect(url, port)
	def getClient(self) :
		return self.client
	def closeClient(self, client) :
		client.close()
