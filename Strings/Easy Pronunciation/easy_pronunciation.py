def solve(lenght, text):
    if lenght <= 3:
        return "YES"
    
    vowels = 'aeiou'
    consonants = 0

    for char in text:
        if char not in vowels:
            consonants += 1
            if consonants == 4:
                break
        else:
            consonants = 0

    if consonants == 4:
        return "NO"
    else: 
        return "YES"

test_cases = int(input())

for i in range(test_cases):
    string_lenght = int(input())
    string = input()
    print(solve(string_lenght, string))