def solution(sizes):
    answer = 0
    x, y = 0, 0
    for i in sizes:
        i.sort()
        if i[0] > x:
            x = i[0]
        if i[1] > y:
            y = i[1]
    answer = x * y
    return answer