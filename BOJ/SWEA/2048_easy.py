N = int(input())

answer = 0
init_board = []

def product(arr,n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in product(arr,n - 1):
                yield [arr[i]] + next

def move(board, direct):
    if direct == 0:
        for i in range(N):
            for j in range(N):
                if board[i][j] != 0:
                    for k in range(j):
                        if board[i][k] == 0:
                            board[i][k] = board[i][j]
                            board[i][j] = 0
                            break
    elif direct == 1:
        for i in range(N):
            for j in range(N):
                if board[j][i] != 0:
                    for k in range(j):
                        if board[k][i] == 0:
                            board[k][i] = board[j][i]
                            board[j][i] = 0
                            break
    elif direct == 2:
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if board[j][i] != 0:
                    for k in range(N - 1, j - 1, -1):
                        if board[k][i] == 0:
                            board[k][i] = board[j][i]
                            board[j][i] = 0
                            break
    elif direct == 3:
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if board[i][j] != 0:
                    for k in range(N - 1, j - 1, -1):
                        if board[i][k] == 0:
                            board[i][k] = board[i][j]
                            board[i][j] = 0
                            break

def add(board, direct):
    if direct == 0:
        for i in range(N):
            for j in range(N - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1]:
                    board[i][j] *= 2
                    board[i][j + 1] = 0
    elif direct == 1:
        for i in range(N):
            for j in range(N - 1):
                if board[j][i] != 0 and board[j][i] == board[j + 1][i]:
                    board[j][i] *= 2
                    board[j + 1][i] = 0
    elif direct == 2:
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, 0, -1):
                if board[j][i] != 0 and board[j][i] == board[j - 1][i]:
                    board[j][i] *= 2
                    board[j - 1][i] = 0
    elif direct == 3:
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, 0, -1):
                if board[i][j] != 0 and board[i][j] == board[i][j - 1]:
                    board[i][j] *= 2
                    board[i][j - 1] = 0

def check(board):
    global answer
    for i in board:
        if max(i) >= answer:
            answer = max(i)

def copy(temp, init):
    for i in range(len(init)):
        for j in range(len(init)):
            temp[i][j] = init[i][j]
    return temp

for _ in range(N):
    init_board.append(list(map(int,input().split())))

cases =[0,1,2,3]

case_list = list(product(cases, 5))


for i in case_list:
    temp = [[0] * N for _ in range(N)]
    board = copy(temp,init_board)
    for j in i:
        move(board,j)
        add(board,j)
        move(board,j)
    check(board)

print(answer)