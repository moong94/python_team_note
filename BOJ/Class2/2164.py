import sys

from collections import deque


n = int(sys.stdin.readline())

card = [i for i in range(1,n + 1)]

queue = deque(card)

if n == 1:
    print(queue.pop())

else:
    while queue:

        queue.popleft()

        x = queue.popleft()
        if len(queue) == 0:
            break
        queue.append(x)
    
    print(x)