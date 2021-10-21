def solution(line):
    answer = []
    cross_x = []
    cross_y = []
    for i in range(len(line)):
        for j in range(i + 1,len(line)):
            x_y_bot = line[i][0] * line[j][1] - line[i][1] * line[j][0]
            x_top = line[i][1] * line[j][2] - line[i][2] * line[j][1]
            y_top = line[i][2] * line[j][0] - line[i][0] * line[j][2]
            if x_y_bot == 0:
                continue
            x = x_top / x_y_bot
            y = y_top / x_y_bot
            if x.is_integer() and y.is_integer():
                cross_x.append(x)
                cross_y.append(y)
    min_x, max_x = min(cross_x), max(cross_x)
    min_y, max_y = min(cross_y), max(cross_y)
    row = int(max_x - min_x + 1)
    col = int(max_y - min_y + 1)
    answer = ["." * int(row) for _ in range(int(col))]
    for i in range(len(cross_x)):
        answer[col - int(cross_y[i] - min_y) - 1] = answer[col - int(cross_y[i] - min_y) - 1][:int(cross_x[i] - min_x)] + "*" + answer[col - int(cross_y[i] - min_y) - 1][int(cross_x[i] - min_x) + 1:]
    
    return answer