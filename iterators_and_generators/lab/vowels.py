class vowels:

    def __init__(self, text):
        self.text = text
        self.all_vowels = ["a", "i", "e", "u", "o", "y"]
        self.start_index = -1
        self.end_index = len(self.text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index += 1

        if self.start_index > self.end_index:
            raise StopIteration

        current_char = self.text[self.start_index]
        if current_char.lower() in self.all_vowels:
            return current_char

        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
