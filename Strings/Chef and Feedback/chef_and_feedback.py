test_cases = int(input())

for i in range(test_cases):
    text = input()
    if '010' in text or '101' in text:
        print('Good')
    else: 
        print('Bad')