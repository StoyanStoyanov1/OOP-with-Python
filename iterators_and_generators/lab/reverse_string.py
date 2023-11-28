def reverse_text(text):
    start_index = len(text) - 1
    end_index = 0

    while start_index >= end_index:
        yield text[start_index]
        start_index -= 1


for char in reverse_text("step"):
    print(char, end='')
