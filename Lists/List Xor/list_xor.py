def list_xor(n, list1, list2):
    if n in list1 and n in list2:
        return False
    if n not in list1 and n not in list2:
        return False
    return True


print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))
