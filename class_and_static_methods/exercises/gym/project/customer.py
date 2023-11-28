class Customer:
    id = 1

    def __init__(self, name, address, email):
        self.id = Customer.get_next_id()
        self.name = name
        self.address = address
        self.email = email

    @staticmethod
    def get_next_id():
        current_id = Customer.id
        Customer.id += 1
        return current_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"