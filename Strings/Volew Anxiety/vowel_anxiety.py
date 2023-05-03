def solve(length, text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    left = ''
    right = ''
    back = True

    for char in text:
        if back:
            right += char
        else:
            left += char
        if char in vowels:
            back = not back
    right = right[::-1]

    return left + right


test_cases = int(input())

for i in range(test_cases):
    string_length = int(input())
    string = input()[::-1]
    print(solve(string_length, string))
