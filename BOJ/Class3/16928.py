from collections import deque

n, m = map(int,input().split())

INF = int(1e9)

distance = [INF] * 101
distance[1] = 0
visited = [False] * 101
visited[1] = True

ladder = []
snake = []

def bfs():
    queue = deque([1])
    while queue:
        now = queue.popleft()
        for i in range(1, 7):
            after = now + i
            if after > 100:
                continue
            if visited[after]:
                continue
            for j in ladder:
                if j[0] == after:
                    after = j[1]
            for j in snake:
                if j[0] == after:
                    after = j[1]
            if not visited[after]:
                visited[after] = True
                distance[after] = distance[now] + 1
                queue.append(after)



for _ in range(n):
    u, v = map(int,input().split())
    ladder.append((u, v))
for _ in range(m):
    u, v = map(int,input().split())
    snake.append((u, v))

bfs()

print(distance[100])