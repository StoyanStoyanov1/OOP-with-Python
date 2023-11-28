from oop.class_and_static_methods.lab.hotel_rooms.project import Drink
from oop.class_and_static_methods.lab.hotel_rooms.project import Food
from oop.class_and_static_methods.lab.hotel_rooms.project import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)