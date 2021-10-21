from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(y, x, board, toggle):
    
    temp = []
    queue = deque()
    queue.append((y,x))
    board[y][x] = 1 - toggle
    while queue:
        y, x = queue.popleft()
        temp.append([y,x])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[ny][nx] == toggle:
                    queue.append((ny,nx))
                    board[ny][nx] = 1 - toggle
    return temp

def point_matching(board):
    for i in board:
        y,x = i[0][0], i[0][1]
        for j in i:
            if j[0] < y:
                y = j[0]
            if j[1] < x:
                x = j[1]
        for k in i:
            k[0] -= y
            k[1] -= x
        i.sort()

def rotate(board):
    for i in board:
        y,x = i[0][0], i[0][1]
        for j in i:
            if j[0] > y:
                y = j[0]
            if j[1] > x:
                x = j[1]
        max_len = max(y, x)
        for j in i:
            j[0],j[1] = j[1], max_len - j[0]
            
def solution(game_board, table):
    answer = 0
    blank_list = []
    block_list = []
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0:
                blank_list.append(bfs(i, j, game_board, 0))
            if table[i][j] == 1:
                block_list.append(bfs(i, j, table, 1))
                
    
    point_matching(blank_list)
    point_matching(block_list)
    
    for i in range(4):
        temp = []
        for j in block_list[:]:
            for k in blank_list[:]:
                if j == k:
                    answer += len(j)
                    blank_list.remove(k)
                    block_list.remove(j)
                    break
                    
        rotate(block_list)
        point_matching(block_list)
    
    return answer