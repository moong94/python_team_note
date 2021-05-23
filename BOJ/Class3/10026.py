from collections import deque

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(x,y, array, s):
    queue = deque([(x,y)])
    array[x][y] = 0
    while queue:
        (x,y) = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >= 0 and nx >= 0 and ny < n and nx < n and array[nx][ny] == s:
                queue.append((nx, ny))
                array[nx][ny] = 0

n = int(input())
rgb = []
rb = [[0] * n for _ in range(n)]

answer_rgb = 0
answer_rb = 0
for i in range(n):
    rgb.append(list(map(str,input())))

for i in range(n):
    for j in range(n):
        if rgb[i][j] == "G" or rgb[i][j] == "R":
            rb[i][j] = 1
        else:
            rb[i][j] = 2

for i in range(n):
    for j in range(n):
        if rgb[i][j] != 0:
            bfs(i,j, rgb, rgb[i][j])
            answer_rgb += 1
        if rb[i][j] != 0:
            bfs(i,j, rb, rb[i][j])
            answer_rb += 1

print(answer_rgb, answer_rb)