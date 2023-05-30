def add_dots(string):
    return('.'.join(string))


def remove_dots(string):
    return ''.join(string.split('.'))


print(add_dots(remove_dots('hello')))
print(remove_dots('b.o.b'))
