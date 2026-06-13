class CustomerDB:
    def __init__(self):
        # initialize an in-memory list to similate a database
        self.customers = []
        self.next_id = 1
        self.connection = None
    
    def connect(self):
        # simulate connecting to a database
        self.connection = "DummyConnectionObject"
        print('Connected to the Database')
    
    def insert_customer(self,name,email):
        # insert new customer in the list
        customer = {
            "id" : self.next_id,
            "name" : name,
            "email" : email
        }
        self.customers.append(customer)
        self.next_id += 1

    def get_all_customers(self):
        # Retieve all customers
        return self.customers
    
    def get_customers_by_name(self,name):
        # get customer by name
        for customer in self.customers:
            if customer['name'] == name:
                return customer
        return None
    
    def clear_customers(self):
        # clear and reset the database/ customer list
        self.customers = []
        self.next_id = 1
    
    def close(self):
        # Simulate closing the database connection
        self.connection = None
        print('Database Connection Closed.')