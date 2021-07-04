import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

def dijkstra(start):
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
                heapq.heappush(queue, (cost, i[0]))

for _ in range(m):
    start, arrive, cost = map(int,input().split())
    graph[start].append((arrive, cost))

init, end = map(int,input().split())

dijkstra(init)

print(distance[end])