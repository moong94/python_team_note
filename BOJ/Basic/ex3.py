def solution(drawing):
    answer = []
    length = len(drawing)
    temp_map = [[0 for _ in range(length)] for _ in range(length)]
    for y in range(length):
        for x in range(length):
            if drawing[y][x] == '1':
                temp_map[y][x] += 1
                temp_map[length - x - 1][y] += 1
                temp_map[x][length - y - 1] += 1
                temp_map[length - y - 1][length - x - 1] += 1
    for i in range(length):
        tmp_string = ''
        for j in range(length):
            tmp_string += str(temp_map[i][j])
        answer.append(tmp_string)
    return answer

print(solution(["11100","00100","00110","00010","00010"]))
print(solution(["1111","1110","1110","0000"]))
print(solution(["010","111","101"]))