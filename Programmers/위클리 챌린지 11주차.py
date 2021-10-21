from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
INF = 1e9

def bfs(graph,start_x,start_y,end_x,end_y):
    queue = deque()
    queue.append([start_y * 2,start_x * 2])
    graph[start_y * 2][start_x * 2] = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[ny][nx] == INF:
                if ny == end_y * 2 and nx == end_x * 2:
                    if graph[ny][nx] != INF:
                        graph[ny][nx] = min(graph[y][x] + 1,graph[ny][nx])
                    else:
                        graph[ny][nx] = graph[y][x] + 1
                    continue
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny,nx])
                
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[0] * 102 for _ in range(102)]
    
    for x_1,y_1,x_2,y_2 in rectangle:
        for i in range(x_1 * 2, x_2 * 2 + 1):
            for j in range(y_1 * 2, y_2 * 2 + 1):
                graph[j][i] = INF
    
    for x_1,y_1,x_2,y_2 in rectangle:
        for i in range(x_1 * 2 + 1, x_2 * 2):
            for j in range(y_1 * 2 + 1, y_2 * 2):
                graph[j][i] = 0
    
    bfs(graph,characterX,characterY, itemX, itemY)
    
    answer = graph[itemY * 2][itemX * 2] // 2
            
    return answer