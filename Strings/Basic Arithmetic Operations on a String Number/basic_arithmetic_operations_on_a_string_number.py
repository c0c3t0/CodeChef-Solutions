def arithmetic_operation(text):
    a, operator, b = text.split(' ')
    a = int(a)
    b = int(b)

    if operator == "*":
        return a * b
    elif operator == "-":
        return a - b
    elif operator == "+":
        return a + b
    elif operator == "//":
        if b != 0:
            return a // b
        else:
            return -1


print(arithmetic_operation('12 + 12'))
print(arithmetic_operation('12 - 12'))
print(arithmetic_operation('12 * 12'))
print(arithmetic_operation('12 // 0'))
