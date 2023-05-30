def all_equal(arr):
    if len(arr) == 0:
        return True
    return len(set(arr)) == 1


print(all_equal([1, 1, 1]))
print(all_equal([]))
