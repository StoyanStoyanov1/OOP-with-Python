from oop.class_and_static_methods.lab.hotel_rooms.project import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = [f"{product.name}: {product.fuel_quantity}" for product in self.products]

        return "\n".join(result)

