test_cases = int(input())


for i in range(test_cases):
    output = ''
    hidden_word, guess_word = input(), input()

    for index in range(len(hidden_word)):
        if hidden_word[index] == guess_word[index]:
            output += 'G'
        else:
            output += 'B'
        
    print(output)
