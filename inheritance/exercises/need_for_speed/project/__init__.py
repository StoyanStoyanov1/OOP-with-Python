food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000


def def_food(current_food):
    return current_food - 300


def def_hay(hay, food):
    hay -= food * 0.05
    return hay


def def_cover(cover, weight):
    cover -= weight * (1 / 3)
    return cover


def logic(food, hay, cover, weight):
    for i in range(1, 30 + 1):
        food = def_food(food)
        if i % 2 == 0:
            hay = def_hay(hay, food)
        if i % 3 == 0:
            cover = def_cover(cover, weight)

    if food or hay or cover < 0:
        food /= 1000
        hay /= 1000
        cover /= 1000
        print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")

    else:
        print("Merry must go to the pet store!")


logic(food, hay, cover, weight)
