import json


class Customer:

    def __init__(self):
        self.customers = []

    def add_customer(self, name, age):
        new_customer = {}
        new_customer["name"] = name
        new_customer["age"] = age
        self.customers.append(new_customer)
        print("customer: {0}".format(new_customer))
        return json.dumps(new_customer)

    def del_customer(self, name):
        found = False
        for idx, customer in enumerate(self.customers):
            if customer["name"] == name:
                index = idx
                found = True
                del self.customers[idx]
        print("customers: {0}".format(json.dumps(self.customers)))
        return found

    def query_customer(self, name):
        found= False
        for idx, customer in enumerate(self.customers):
            if customer["name"] == name:
                index = idx
                found = True
                #age = customer["age"]
                #print(age)
    
        return found

    def dump(self,name):
        for idx, customer in enumerate(self.customers):
            if customer["name"] == name:
                index = idx
        return json.dumps(self.customers[index])
    def get_all_customers(self):
        return self.customers

    def json_list(self):
        return json.dumps(self.customers)
