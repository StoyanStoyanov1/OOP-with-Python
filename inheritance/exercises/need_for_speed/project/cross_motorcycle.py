from oop.inheritance.exercises.need_for_speed.project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)