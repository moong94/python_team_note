from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int,input().split())

boxes = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < m and boxes[nx][ny] == 0:
            boxes[nx][ny] = 1
            init.append((nx,ny))

for _ in range(n):
    boxes.append(list(map(int,input().split())))

init = []
answer = -1
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            init.append((i,j))

while init:
    queue = deque(init)
    init = []
    while queue:
        x,y = queue.popleft()
        bfs(x,y)
    answer += 1

toggle = True

for i in boxes:
    if 0 in i:
        toggle = False
        break

if toggle:
    print(answer)
else:
    print(-1)
