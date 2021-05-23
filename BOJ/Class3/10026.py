from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(x,y, array, s):
    queue= deque()
    queue.append((x,y))
    while queue:
        tmp = queue.popleft()
        x, y = tmp[0], tmp[1]
        array[x][y] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if array[nx][ny] == s:
                queue.append((nx, ny))


rgb = [[0] * (n + 2) for _ in range(n + 2)]
rb = [[0] * (n + 2) for _ in range(n + 2)]

answer_rgb = 0
answer_rb = 0
for i in range(n):
    tmp = input()
    k = 0
    for j in tmp:
        rgb[i + 1][k + 1] = j
        if j == "G":
            rb[i + 1][k + 1] = "R"
        else:
            rb[i + 1][k + 1] = j
        k += 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if rgb[i][j] != 0:
            bfs(i,j, rgb, rgb[i][j])
            answer_rgb += 1
        if rb[i][j] != 0:
            bfs(i,j, rb, rb[i][j])
            answer_rb += 1

print(answer_rgb, answer_rb)