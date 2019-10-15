import tornado.web
from customer import Customer
import json

class QueryHandler(tornado.web.RequestHandler):
	def initialize(self, customers):
		self.customers=customers

	def get(self):
		name=self.get_argument('name')
		result = self.customers.query_customer(name)
		if result:
			self.write("Found customer name: {0} successfully".format(name))
			self.write(self.customers.dump(name))
			self.set_status(200)
		else:
			self.write("customer '{0}' not found".format(name))
			self.set_status(404)

