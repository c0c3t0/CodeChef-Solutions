def capital_indexes(string):
    result = []
    for i in range(len(string)):
        if string[i].isupper():
            result.append(i)
    return result

print(capital_indexes('HeLlO'))