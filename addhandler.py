import tornado.web
from customer import Customer
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, customers):
        self.customers = customers
        
    def get(self):
        name = self.get_argument('name')
        age = self.get_argument('age')
        result = self.customers.add_customer(name, age)
        self.write(result)
