def guess_score(code, guess):
    result = {'black': 0, 'white': 0}

    for i in range(len(code)):
        if code[i] == guess[i]:
            result['black'] += 1
        elif code[i] in guess:
            result['white'] += 1
    return result


print(guess_score('1423', '5678'))
print(guess_score('1423', '2222'))
print(guess_score('1423', '1234'))
print(guess_score('1423', '2211'))
