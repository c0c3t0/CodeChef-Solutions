def only_ints(x, y):
    return type(x) is int and type(y) is int

print(only_ints(1, 2))
print(only_ints("a", 2))
print(only_ints(True, 1))