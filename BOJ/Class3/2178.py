import sys
from collections import deque



n, m = map(int,input().split())

maze = []

maze.append([0] * (m + 2))

for _ in range(n):
    tmp = [0]
    x = input()
    for i in x:
        tmp.append(int(i))
    tmp.append(0)
    maze.append(tmp)

maze.append([0] * (m + 2))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

bfs(1,1)

print(maze[n][m])