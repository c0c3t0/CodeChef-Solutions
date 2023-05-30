def consecutive_zeros(x):
    return len(max(x.split('1')))


print(consecutive_zeros("1001101000110"))