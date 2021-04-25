import sys

t = int(input())
# 재귀 함수 최대 깊이 제한 변경
sys.setrecursionlimit(10 ** 6)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def search(array,x,y):

    array[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if array[nx][ny] == 1:
            search(array, nx, ny)

for _ in range(t):
    m, n, k = map(int,input().split())

    ground = [[0] * (m + 2) for _ in range(n + 2)]

    warm = 0

    for _ in range(k):
       x, y = map(int,input().split())
       ground[y + 1][x + 1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if ground[i][j] == 1:
                search(ground, i, j)
                warm += 1


    print(warm)

