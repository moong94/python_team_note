n, m = map(int,input().split())

ice_board = []
for _ in range(n):
    ice_board.append(list(map(int, input())))

answer = 0

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if ice_board[x][y] == 0:
        ice_board[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for x in range(n):
    for y in range(m):
        if dfs(x,y) == True:
            answer += 1

print(answer)

