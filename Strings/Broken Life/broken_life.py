def solve(first_len, second_len, str_s, str_a):
    result = []
    j = 0
    chars = {'a', 'b', 'c', 'd', 'e'}

    for i in range(first_len):
        if str_s[i] == str_a[j]:
            result.append(str_s[i])
            j += 1
            if j == second_len:
                return '-1'
        elif str_s[i] == '?':
            l = chars-{str_a[j]}
            result.append((chars-{str_a[j]}).pop())
        else:
            result.append(str_s[i])

    return ''.join(result)


for case in range(int(input())):
    first_len, second_len = list(map(int, input().split()))
    str_S = input()
    str_A = input()
    print(solve(first_len, second_len, str_S, str_A))
