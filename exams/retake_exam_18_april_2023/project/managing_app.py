from exams.exam_10_december_2022.project import Route
from exams.exam_10_december_2022.project import User
from exams.exam_10_december_2022.project import CargoVan
from exams.exam_10_december_2022.project import PassengerCar


class ManagingApp:
    VAlID_VEHICLE_TYPE = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []
    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self._find_user_by_driving_license_number(driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VAlID_VEHICLE_TYPE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self._find_vehicle_by_license_plate_number(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VAlID_VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        result = self._find_route_by_point_and_length(start_point, end_point, length)
        if result:
            return result

        route_id = len(self.routes) + 1

        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int, is_accident_happened: bool):
        user = self._find_user_by_driving_license_number(driving_license_number)
        vehicle = self._find_vehicle_by_license_plate_number(license_plate_number)
        route = self._find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()

        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))[:count]
        for vehicle in selected_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
        return f"{len(selected_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        sorted_users = sorted(self.users, key=lambda user: -user.rating)
        for user in sorted_users:
            result.append(user.__str__())

        return '\n'.join(result)

    def _find_user_by_driving_license_number(self, license_number):
        for user in self.users:
            if user.driving_license_number == license_number:
                return user

    def _find_vehicle_by_license_plate_number(self, license_plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return vehicle

    def _find_route_by_point_and_length(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

    def _find_route_by_id(self, route_id):
        for route in self.routes:
            if route.route_id == route_id:
                return route
