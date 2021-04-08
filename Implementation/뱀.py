n = int(input())    # 보드의 크기 n
k = int(input())    # 사과의 갯수 k

board = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(n + 2):
    for j in range(n + 2):
        if i == 0 or i == n + 1 or j == 0 or j == n + 1:
            board[i][j] = 1

for _ in range(k):
    row, column = map(int, input().split())
    board[row][column] = 2

l = int(input())

snake_move = []

for _ in range(l):
    x, c = input().split()
    snake_move.append([int(x), c])

snake = [1,1,0]     # row, column, direct
snake_loc = [[1,1]]
board[1][1] = 1
answer = 0
    # 동 남 서 북
dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]



def solution(snake, snake_move, snake_loc, board):
    global answer
    global dx
    global dy
    idx = 0
    while True:

        if snake[2] == 4:
            snake[2] = 0
        elif snake[2] == -1:
            snake[2] = 3
        while True:
            answer += 1
            snake[0] += dy[snake[2]]
            snake[1] += dx[snake[2]]
            if board[snake[0]][snake[1]] == 1:
                return answer
            elif board[snake[0]][snake[1]] == 2:
                board[snake[0]][snake[1]] = 1
                snake_loc.insert(0, [snake[0], snake[1]])
            else:
                board[snake[0]][snake[1]] = 1
                board[snake_loc[-1][0]][snake_loc[-1][1]] = 0
                snake_loc.pop()
                snake_loc.insert(0, [snake[0], snake[1]])

            for i in range(len(board)):
                for j in range(len(board)):
                    print(board[i][j], end="")
                print()
            print()

            if len(snake_move) != 0:
                if snake_move[0][0] == answer:
                    break

        if snake_move[0][1] == "L":
            snake[2] -= 1
        elif snake_move[0][1] == "D":
            snake[2] += 1

        snake_move.pop(0)

print(solution(snake, snake_move, snake_loc, board))



