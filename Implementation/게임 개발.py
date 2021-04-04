n, m = map(int, input().split())

x, y, direction = map(int,input().split())

now = [[0] * m for _ in range(n)]

now[x][y] = 1

game = []
for i in range(n):
    game.append(list(map(int, input().split())))
    # 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction -= 1
count = 0
answer = 0

while True:
    if direction < 0:
        direction = 3

    if game[x + dx[direction]][y + dy[direction]] == 1:
        count += 1
    else:
        x += dx[direction]
        y += dy[direction]

        now[x][y] = 1
        game[x][y] = 1
        count = 0

    if count == 4:
        if game[x - dx[direction]][y - dy[direction]] == 1:
            break
        else:
            x -= dx[direction]
            y -= dy[direction]

            now[x][y] = 1
            game[x][y] = 1
            count = 0

    direction -= 1

for i in range(n):
    answer += now[i].count(1)

print(answer)


