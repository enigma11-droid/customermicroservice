import tornado.web
from customer import Customer
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, customers):
    	self.customers = customers
        
    def get(self):
        self.write(self.customers.json_list())
