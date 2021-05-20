from collections import deque

n = int(input())

houses = [[0] * (n + 2) for _ in range(n + 2)]

answer_case = []

for i in range(n):
    tmp = input()
    for j in range(len(tmp)):
        houses[i + 1][j + 1] = int(tmp[j])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 0
    while queue:
        tmp= queue.popleft()
        if houses[tmp[0]][tmp[1]] == 1:
            count += 1
            houses[tmp[0]][tmp[1]] = 0
        else:
            continue
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if houses[nx][ny] == 1:
                queue.append((nx,ny))

    answer_case.append(count)


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if houses[i][j] == 1:
            bfs(i,j)

answer_case.sort()

print(len(answer_case))
for i in answer_case:
    print(i)