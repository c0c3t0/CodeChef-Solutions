test_cases = int(input())


for i in range(test_cases):
    frames = int(input())
    frames_values = input().split()
    result = 1

    for fr in range(frames - 1):
        if frames_values[fr] != frames_values[fr+1]:
            result += 1
            
    print(result)
