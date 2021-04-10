from itertools import combinations

n, m = map(int, input().split())

lab = []

for _ in range(n):
    lab.append(list(map(int,input().split())))

space_list = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            space_list.append((i,j))

install = list(combinations(space_list, 3))

answer_case = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if lab_test[nx][ny] == 0:
            lab_test[nx][ny] = 2
            dfs(nx,ny)

def count(lab_test):
    zero_count = 0
    for i in range(n):
        for j in range(m):
            if lab_test[i][j] == 0:
                zero_count += 1
    return zero_count

lab_test = [[0] * m for _ in range(n)]

for case in install:

    for i in range(n):
        for j in range(m):
            lab_test[i][j] = lab[i][j]

    # 빈 공간의 3개의 벽 설치
    for install_wall in case:
        lab_test[install_wall[0]][install_wall[1]] = 1

    for i in range(n):
        for j in range(m):
            if lab_test[i][j] == 2:
                dfs(i,j)

    answer_case.append(count(lab_test))

print(max(answer_case))



