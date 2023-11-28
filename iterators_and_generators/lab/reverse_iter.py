class reverse_iter:

    def __init__(self, obj):
        self.obj = obj
        self.start_index = len(self.obj)
        self.end_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index -= 1
        if not self.start_index < self.end_index:
            return self.obj[self.start_index]

        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
