from collections import deque

n, k = map(int,input().split())

loc = 0

data = [i for i in range(1,n + 1)]

queue = deque(data)

print("<",end="")
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    if len(queue) == 1:
        print(queue.popleft(),end=">")
    else:
        print(queue.popleft(),end=", ")

