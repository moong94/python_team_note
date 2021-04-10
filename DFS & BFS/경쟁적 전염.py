n, k = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

s, x, y = map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

temp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        temp[i][j] = data[i][j]

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if temp[nx][ny] == 0:
            temp[nx][ny] = temp[x][y]

count = 0

while count < s:
    for virus in range(1,k + 1):
        for i in range(n):
            for j in range(n):
                if data[i][j] == virus:
                    dfs(i,j)



    count += 1

    for i in range(n):
        for j in range(n):
            data[i][j] = temp[i][j]

print(data[x - 1][y - 1])






