from exams.exam_10_december_2022.project import FemaleRobot
from exams.exam_10_december_2022.project import MaleRobot
from exams.exam_10_december_2022.project import MainService
from exams.exam_10_december_2022.project import SecondaryService


class RobotsManagingApp:
    ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
    SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.SERVICE_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = self._find_service_by_name(service_name)
        robot = self._find_robot_by_name(robot_name)

        if robot.POSSIBLE_SERVICE != service.__class__.__name__:
            return "Unsuitable service."

        if not service.capacity > len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._find_service_by_name(service_name)
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        current_robot = robot[0]
        service.robots.remove(current_robot)
        self.robots.append(current_robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._find_service_by_name(service_name)
        number_of_robots_fed = len([r.eating() for r in service.robots])
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = self._find_service_by_name(service_name)
        total_price = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = [service.details() for service in self.services]
        return '\n'.join(result)

    def _find_robot_by_name(self, name):
        for r in self.robots:
            if r.name == name:
                return r

    def _find_service_by_name(self, name):
        for s in self.services:
            if s.name == name:
                return s
