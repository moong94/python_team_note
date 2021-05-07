import sys
from collections import deque

input = sys.stdin.readline

def bfs(x):
    queue = deque([x])
    while queue:
        x = queue.popleft()
        if virused[x] == 0:
            virused[x] = 1
            for i in graph[x]:
                if virused[i] == 0:
                    queue.append(i)



n = int(input())

m = int(input())

graph = [[] for _ in range(n + 1)]

virused = [0] * (n + 1)

for _ in range(m):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


for i in graph:
    i.sort()

bfs(1)

print(sum(virused) - 1)