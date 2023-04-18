test_cases = int(input())

for i in range(test_cases):
    initial_length = int(input())
    string = input()

    length = initial_length // 2
    first_part, last_part = string[:length], string[length:]

    if first_part == last_part:    
        print('YES') 
    else:
        print('NO')