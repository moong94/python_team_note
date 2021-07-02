import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

t = int(input())


def solution(graph):
    distance = [[INF] * (len(graph)) for _ in range(len(graph))]

    x,y = 0,0

    queue = [(graph[x][y],x,y)]

    while queue:
        dist, x, y = heapq.heappop(queue)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(queue,(cost,nx,ny))
    for i in range(len(graph)):
        print(*distance[i])
    return distance[-1][-1]



for _ in range(t):
    n = int(input())

    graph = [list(map(int,input().split())) for _ in range(n)]

    print(solution(graph))

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
