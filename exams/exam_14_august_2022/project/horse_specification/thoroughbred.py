from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def max_speed(self):
        return 140

    def train(self):
        train_speed = self.speed + 3
        self.speed = min(train_speed, self.max_speed())

