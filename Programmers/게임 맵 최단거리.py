from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,maps):
    queue = deque([(y,x)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < len(maps[0]) and ny >= 0 and ny < len(maps):
                if nx == 0 and ny == 0:
                    continue
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((ny,nx))

def solution(maps):
    answer = 0
    
    bfs(0,0,maps)
    if maps[-1][-1] == 1:
        return -1
    else:
        answer = maps[-1][-1]
    return answer