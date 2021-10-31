def solution(dirs):
    answer = 0
    maps = [[0] * 21 for _ in range(21)]
    y,x = 10,10
    maps[y][x] = 1
    for i in dirs:
        if i == "U":
            if y < 20:
                y += 1
                if maps[y][x] == 0:
                    answer += 1
                    maps[y][x] = 1
                y += 1
                maps[y][x] = 1
        elif i == "D":
            if y > 0:
                y -= 1
                if maps[y][x] == 0:
                    answer += 1
                    maps[y][x] = 1
                y -= 1
                maps[y][x] = 1
        elif i == "L":
            if x > 0:
                x -= 1
                if maps[y][x] == 0:
                    answer += 1
                    maps[y][x] = 1
                x -= 1
                maps[y][x] = 1
        elif i == "R":
            if x < 20:
                x += 1
                if maps[y][x] == 0:
                    answer += 1
                    maps[y][x] = 1
                x += 1
                maps[y][x] = 1
    
    return answer