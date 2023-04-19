test_cases = int(input())


for i in range(test_cases):
    digits = int(input())
    number = input()
    is_multiple_of_5 = False

    for d in range(digits):
            for n in number:
                if int(n) == 5 or int(n) == 0:
                    is_multiple_of_5 = True
                    break

    if is_multiple_of_5:
        print('Yes')
    else:
        print('No')
