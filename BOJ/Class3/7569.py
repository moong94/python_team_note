from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int,input().split())

boxes = []
answer = -1
zero_count = 0
init = []

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,n,-n]

def bfs(y,x):
    global zero_count
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < (n * h) and boxes[ny][nx] == 0:
            if (y % n == 0 and ny % n == (n - 1)) or (y % n == (n - 1) and ny % n == 0):
                continue
            else:
                boxes[ny][nx] = 1
                init.append((ny,nx))
                zero_count -= 1


for _ in range(n * h):
    arr = list(map(int,input().split()))
    boxes.append(arr)

for i in range(n * h):
    for j in range(m):
        if boxes[i][j] == 0:
            zero_count += 1
        elif boxes[i][j] == 1:
            init.append((i,j))

while init:
    queue = deque(init)
    init = []
    while queue:
        y,x = queue.popleft()
        bfs(y,x)
    answer += 1

if zero_count != 0:
    print(-1)
else:
    print(answer)