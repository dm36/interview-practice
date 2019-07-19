def square(x):
    return x**2

print map(lambda x: x**2, [1, 2, 3, 4, 5])
print list(map(lambda x: x**2, [1, 2, 3, 4, 5]))

print list(map(square, [1, 2, 3, 4, 5]))
