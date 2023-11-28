def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}{tuple(args)}\n" \
               f"it returned {func(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
