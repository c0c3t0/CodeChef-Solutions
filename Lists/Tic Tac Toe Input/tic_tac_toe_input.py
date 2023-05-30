def get_row_col(input):
    col = {
        'A': 0,
        'B': 1,
        'C': 2
    }
    row = {
        '1': 0,
        '2': 1,
        '3': 2
    }

    return row[input[1]], col[input[0]]


print(get_row_col('C1'))
print(get_row_col('A3'))
print(get_row_col('A1'))
print(get_row_col('B1'))
