from exams.exam_10_december_2022.project import Customer
from exams.exam_10_december_2022.project import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) == MovieWorld.customer_capacity():
            return
        self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) == MovieWorld.dvd_capacity():
            return
        self.dvds.append(dvd)

    def find_customer_by_id(self, current_id):
        for customer in self.customers:
            if customer.id == current_id:
                return customer

    def find_dvd_by_id(self, current_id):
        for dvd in self.dvds:
            if dvd.id == current_id:
                return dvd

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        return "\n".join(repr(x) for x in self.customers) + "\n" + '\n'.join(repr(x) for x in self.dvds)
