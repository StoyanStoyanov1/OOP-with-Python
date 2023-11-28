from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def max_speed(self):
        return 120

    def train(self):
        train_speed = self.speed + 2
        self.speed = min(train_speed, self.max_speed())
