from exams.exam_10_december_2022.project import Customer
from exams.exam_10_december_2022.project import Equipment
from exams.exam_10_december_2022.project import ExercisePlan
from exams.exam_10_december_2022.project import Gym
from exams.exam_10_december_2022.project import Subscription
from exams.exam_10_december_2022.project import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")

subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)
gym = Gym()
gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)
print(Customer.get_next_id())
print(gym.subscription_info(1))