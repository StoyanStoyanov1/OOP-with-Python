def print_up(size):
    for row in range(1, size + 1):
        for space in range(size - row):
            print(" ", end="")
        for star in range(1, row):
            print("*", end=" ")
        print("*")


def print_bottom(size):
    for row in range(size - 1, 0, -1):
        for space in range(size - row):
            print(f" ", end="")
        for star in range(1, row):
            print("*", end=" ")
        print("*")

size = int(input())
print_up(size)
print_bottom(size)