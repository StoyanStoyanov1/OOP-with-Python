class Hero:

    def __init__(self, username, level):
        self.level = level
        self.username = username

    def __str__(self):
        return f"{self.username} of type {Hero.__name__} has level {self.level}"