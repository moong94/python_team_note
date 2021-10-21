from collections import deque

def bfs(start, graph):
    visited = [False] * len(graph)
    queue = deque([start])
    cnt = 0
    visited[start] = True
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt

def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        cuted_wires = wires[:i] + wires[i + 1:]
        graph = [[] for _ in range(n + 1)]
        for j in cuted_wires:
            graph[j[0]].append(j[1])
            graph[j[1]].append(j[0])
        
        con = bfs(1,graph)
        res = n - con
        if abs(res - con) < answer:
            answer = abs(res - con)
        
        
    return answer