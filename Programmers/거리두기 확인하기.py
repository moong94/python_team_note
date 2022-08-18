dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(y, x, maps, cases, between):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < 5 and ny < 5:
            if maps[ny][nx] == 'O':
                maps[ny][nx] = 'X'
                dfs(ny,nx,maps, cases, between + 1)
                maps[ny][nx] = 'O'
            elif maps[ny][nx] == 'P':
                cases.append(between)
    return cases

def solution(places):
    answer = []
    for i in range(5):
        print(i)
        temp_map = places[i].copy()
        temp = []
        ex = 1
        for j in range(5):
            temp.append(list(temp_map[j]))
        cases = []
        print()
        for y in range(5):
            for x in range(5):
                if temp[y][x] == 'P':
                    temp[y][x] = 'X'
                    cases = dfs(y,x, temp, cases, 1)
                    temp[y][x] = 'P'
                    if cases:
                        if min(cases) <= 2:
                            ex = 0
                            break
                    for k in range(5):
                        temp.append(list(temp_map[k]))
                    cases = []
        answer.append(ex)
    return answer