from collections import deque

for i in range(int(input())):
    string = input()

    def left_shift(text):
        text = deque(text)
        text.append(text.popleft())
        return ''.join(text)

    def right_shift(text):
        text = deque(text)
        text.appendleft(text.pop())
        return ''.join(text)

    left = left_shift(string)
    right = right_shift(string)

    if left == right:
        print('YES')
    else:
        print('NO')
