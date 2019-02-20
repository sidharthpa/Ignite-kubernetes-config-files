from pyignite import Client

class Database:
	def __init__(self, url='127.0.0.1', port=10800) :
		self.client = Client()
		self.client.connect(url, port)
	def getData(self, query_str, query_args=None, include_field_names=True) :
		return self.client.sql(query_str=query_str, query_args=query_args, include_field_names=include_field_names)
	def runQuery(self, query_str, query_args=None, include_field_names=True) :
		return self.client.sql(query_str=query_str, query_args=query_args, include_field_names=include_field_names)