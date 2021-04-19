from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    important = list(map(int,input().split()))

    queue = deque(important)
    count = 0
    while count < n:
        max_num = max(queue)
        a = queue.popleft()
        m -= 1
        if a != max_num:
            queue.append(a)
        else:
            if m == -1:
                count += 1
                print(count)
                break
            else:
                count += 1
                continue
        if m < 0:
            m = len(queue) - 1