from exams.exam_10_december_2022.project import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    TYPE = "CargoVan"
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage):
        self.battery_level -= (round(mileage / self.MAX_MILEAGE * 100) + 5)




