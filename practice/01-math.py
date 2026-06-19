def add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")


def subtract(x, y):
    result = x - y
    print(f"{x} - {y} = {result}")


def multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")


def divide(x, y):
    if y == 0:
        print("Error. Dividend cannot be zero")
    else:
        result = x / y
        print(f"{x} / {y} = {result}")


add(1, 2)
subtract(10, 7)
multiply(4, 2)
divide(10, 2)
divide(15, 0)
