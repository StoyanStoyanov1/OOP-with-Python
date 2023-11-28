class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.count - 1:
            raise StopIteration

        self.start += 1

        return self.start * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
