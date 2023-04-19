test_cases = int(input())

for i in range(test_cases):
    text = input()
    count = 0
    max_count = 0



    for v in text:
        if v in ('aeiou'):
            count += 1
        
            if count > max_count: 
                max_count = count
        else:
            count = 0

    if max_count > 2:
        print('Happy')
    else:
        print('Sad')