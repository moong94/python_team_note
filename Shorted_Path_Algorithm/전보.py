import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int,input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int,input().split())
    # x에서 y도시로 z시간만큼
    graph[x].append((y,z))

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0, start))
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

dijkstra(c)

cities = 0
times = 0
for i in distance:
    if i < INF:
        cities += 1
        times = max(times,i)

print(cities - 1, times)