from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

count = 0

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if not(visited[v]):
            visited[v] = True
            for i in graph[v]:
                if not (visited[i]):
                    queue.append(i)

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1,n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)