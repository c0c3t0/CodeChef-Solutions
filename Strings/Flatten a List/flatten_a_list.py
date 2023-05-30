def flatten(matrix):
    return [item for el in matrix for item in el]


print(flatten([[1, 2], [3, 4]]))
