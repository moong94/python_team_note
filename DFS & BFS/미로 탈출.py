from collections import deque

n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int,input())))


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        for i in range(n):
            print(maze[i])
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
        print()
    return(maze[n - 1][m - 1])

print(bfs(0,0))
