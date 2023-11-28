class sequence_repeat:

    def __init__(self, text, number):
        self.text = text
        self.number = number
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index >= self.number:
            raise StopIteration

        return self.text[self.current_index % len(self.text)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
