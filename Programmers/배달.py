import heapq

INF = 1e9

def dijkstra(graph, start):
    visited = [False] * len(graph)
    costs = [INF] * len(graph)
    costs[start] = 0
    queue = []
    heapq.heappush(queue,(0, start))
    while queue:
        cost, now = heapq.heappop(queue)
        if visited[now]:
            continue
        for i in graph[now]:
            if i[0] + cost < costs[i[1]]:
                heapq.heappush(queue,(cost + i[0], i[1]))
                costs[i[1]] = i[0] + cost
        visited[now] = True
    return costs
    
    
def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N + 1)]
    
    for i in road:
        graph[i[0]].append((i[2],i[1]))
        graph[i[1]].append((i[2],i[0]))
    
    costs = dijkstra(graph,1)
    for i in costs:
        if i <= K:
            answer += 1
    return answer