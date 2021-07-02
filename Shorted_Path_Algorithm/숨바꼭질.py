import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
distance = [INF] * (n + 1)
distance[0] = -1

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dikjstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

dikjstra(1)

idx = distance.index(max(distance))

print(idx, distance[idx], distance.count(distance[idx]))
