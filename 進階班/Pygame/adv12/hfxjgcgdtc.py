numbers = [1, 2, 3]
print(numbers)
print(*numbers)


def add(a, b, c):
    return a + b + c


numbers = [1, 2, 3]
result = add(*numbers)
print(result)


def get_coordinates():
    return 10, 20


print(get_coordinates())
x, y = get_coordinates()
print(x)
print(y)
print(*get_coordinates())
