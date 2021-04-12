from itertools import combinations

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input().split())))

space_list = []

for i in range(n):
    for j in range(n):
        if board[i][j] == "X":
            space_list.append((i,j))

space_combi = list(combinations(space_list,3))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

temp = [[0] * n for _ in range(n)]

def find(x,y):
    for i in range(4):
        ex = x
        ey = y
        while True:
            nx = ex + dx[i]
            ny = ey + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break

            if temp[nx][ny] == "S":
                return False
            elif temp[nx][ny] == "O":
                break
            else:
                ex = nx
                ey = ny
    return True

teacher_count = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == "T":
            teacher_count += 1

no_toggle = 0

for case in space_combi:
    count = 0
    # 맵 초기화
    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]

    for i in range(3):
        temp[case[i][0]][case[i][1]] = "O"

    for i in range(n):
        for j in range(n):
            if temp[i][j] == "T":
                if find(i,j):
                    count += 1

    if count == teacher_count:
        print("YES")
        no_toggle += 1
        break

if no_toggle == 0:
    print("NO")
