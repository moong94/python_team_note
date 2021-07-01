n, m = map(int,input().split())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

x, k = map(int,input().split())

answer = 0

answer = graph[1][k] + graph[k][x]

if answer >= INF:
    answer = -1

print(answer)