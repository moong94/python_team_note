dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(rows, columns, queries):
    answer = []
    maps = []
    for i in range(rows):
        maps.append([i * columns + (j+1) for j in range(columns)])
    
    
    for i in queries:
        y1, x1, y2, x2 = i
        cnt = 0
        j = 0
        x, y = x1 - 1, y1 - 1
        row = x2 - x1
        column = y2 - y1
        temp = maps[y][x]
        min_num = rows * columns
        while cnt < ((x2 - x1) + (y2 - y1)) * 2:
            if temp < min_num:
                min_num = temp
            nx = x + dx[j]
            ny = y + dy[j]
            temp, maps[ny][nx] = maps[ny][nx], temp
            y, x = ny, nx
            cnt += 1
            if cnt == row or cnt == row + column or cnt == row * 2 + column:
                j += 1
        answer.append(min_num)
    return answer