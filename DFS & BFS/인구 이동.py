from collections import deque

n, l, r = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer = 0

def bfs(x,y,index):
    union = []
    union.append((x,y))

    queue = deque()
    queue.append((x,y))

    temp[x][y] = index
    summary = graph[x][y]
    country = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < n and temp[nx][ny] == -1:
                if l <= abs(graph[x][y] - graph[nx][ny]) and abs(graph[x][y] - graph[nx][ny]) <= r:
                    queue.append((nx,ny))
                    temp[nx][ny] = index
                    summary += graph[nx][ny]
                    country += 1
                    union.append((nx,ny))
    for i, j in union:
        graph[i][j] = summary // country
    return country


count = 0

while True:
    temp = [[-1] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if temp[i][j] == -1:
                bfs(i,j,index)
                index += 1
    if index == n * n:
        break
    count += 1

print(count)