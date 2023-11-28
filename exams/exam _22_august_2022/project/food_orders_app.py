from typing import List

from project.meals.meal import Meal
from project.client import Client
from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert


class FoodOrdersApp:
    POSSIBLE_MEALS = {'Starter': Starter, 'MainDish': MainDish, 'Dessert': Dessert}
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str) -> str:
        if self.find_client_by_phone_number(client_phone_number, self.clients_list):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal) -> None:

        for meal in meals:
            if meal.__class__.__name__ in self.POSSIBLE_MEALS:
                self.menu.append(meal)

    def show_menu(self) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        details_for_each_meal = [meal.details() for meal in self.menu]
        return '\n'.join(details_for_each_meal)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self.find_client_by_phone_number(client_phone_number, self.clients_list)

        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        shopping_cart = []
        bill = 0

        for meal_name, quantity in meal_names_and_quantities.items():
            current_meal = self.find_meal_by_name(meal_name, self.menu)

            if not current_meal:
                raise Exception(f"{meal_name} is not on the menu!")

            if current_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {current_meal.TYPE}: {meal_name}!")
            ordered_meal = self.POSSIBLE_MEALS[current_meal.TYPE](meal_name, current_meal.price, quantity)
            shopping_cart.append(ordered_meal)
            bill += current_meal.price * quantity

        client.bill += bill
        client.shopping_cart.extend(shopping_cart)
        meal_names = [meal.name for meal in client.shopping_cart]
        client_list = {}

        for meal in client.shopping_cart:
            if meal.name not in client_list:
                client_list[meal.name] = 0

            client_list[meal.name] += meal.quantity

        for client_name, quantity in client_list.items():
            for meal in self.menu:
                if meal.name == client_name:
                    meal.quantity -= quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str) -> str:
        client = self.find_client_by_phone_number(client_phone_number, self.clients_list)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client_list = {}

        for meal in client.shopping_cart:
            if meal.name not in client_list:
                client_list[meal.name] = 0

            client_list[meal.name] += meal.quantity

        for client_name, quantity in client_list.items():
            for meal in self.menu:
                if meal.name == client_name:
                    meal.quantity += quantity

        client.shopping_cart = []
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.find_client_by_phone_number(client_phone_number, self.clients_list)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        total_sum = client.bill
        client.bill = 0
        client.shopping_cart = []

        return f"Receipt #{self.receipt_id} with total amount of {total_sum:.2f} was successfully paid for {client_phone_number}."

    @staticmethod
    def find_client_by_phone_number(phone_number, clients_list):
        for client in clients_list:
            if client.phone_number == phone_number:
                return client

    @staticmethod
    def find_meal_by_name(meal_name, menu):
        for meal in menu:
            if meal.name == meal_name:
                return meal


    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
