N = int(input())
K = int(input())

board = [[0] * (N + 2) for _ in range(N + 2)]

for i in range(len(board)):
    board[0][i] = 2
    board[i][0] = 2
    board[len(board) - 1][i] = 2
    board[i][len(board) - 1] = 2

for _ in range(K):
    x, y = map(int,input().split())
    board[y][x] = 1

print(board)
L = int(input())

move_list = []

snake_length = 1
s_x, s_y = 1, 1
    # 오 아 왼 위
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]

direction = 0

board[s_y][s_x] = 3

for _ in range(L):
    sec, direct = map(str,input().split())
    move_list.append([int(sec), direct])

for i in move_list:
    for j in i[0]:
        board[s_y][s_x]

