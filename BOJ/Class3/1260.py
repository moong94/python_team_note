from collections import deque

n, m, v = map(int,input().split())

def dfs(v):
    print(v, end = " ")
    visited_dfs[v] = True
    for i in graph[v]:
        if not(visited_dfs[i]):
            dfs(i)


def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if not(visited_bfs[v]):
            visited_bfs[v] = True
            print(v, end = " ")
            for i in graph[v]:
                if not (visited_bfs[i]):
                    queue.append(i)


graph = [[] for _ in range(n + 1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

dfs(v)
print()
bfs(v)