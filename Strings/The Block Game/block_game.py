test_cases = int(input())

for i in range(test_cases):
    num = input()

    if num == num[-1::-1]:
        print('wins')
    else:
        print('loses')