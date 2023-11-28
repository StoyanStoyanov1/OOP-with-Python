from exams.exam_10_december_2022.project import Customer
from exams.exam_10_december_2022.project import Equipment
from exams.exam_10_december_2022.project import ExercisePlan
from exams.exam_10_december_2022.project import Subscription
from exams.exam_10_december_2022.project import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def find_by_id(self, current_id, current_list):
        for obj in current_list:
            if current_id == obj.id:
                return repr(obj)

    def subscription_info(self, subscription_id):
        result = []
        result.append(self.find_by_id(subscription_id, self.subscriptions))
        result.append(self.find_by_id(subscription_id, self.customers))
        result.append(self.find_by_id(subscription_id, self.trainers))
        result.append(self.find_by_id(subscription_id, self.equipment))
        result.append(self.find_by_id(subscription_id, self.plans))

        return '\n'.join(result)