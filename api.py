import tornado.ioloop
import tornado.web
from customer import Customer
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler
from queryhandler import QueryHandler

customers = Customer()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("customers Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addcustomer", AddHandler, dict(customers = customers)),
        (r"/v1/delcustomer", DelHandler, dict(customers = customers)),
        (r"/v1/getcustomers", GetHandler, dict(customers = customers)),
        (r"/v1/querycustomer", QueryHandler, dict(customers = customers)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


#http://localhost:8888/v1/addcustomer?name="Rishikesh Singh"&age="20"
#http://localhost:8888/v1/addcustomer?name="Rashi Sharma"&age="20"
#http://localhost:8888/v1/getcustomers
#ttp://localhost:8888/v1/querycustomer?name="Rishikesh Singh"
#http://localhost:8888/v1/delcustomer?name="Rashi Sharma"
#http://localhost:8888/v1/querycustomer?name="Rashi Sharma"