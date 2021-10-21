def solution(sizes):
    answer = 0
    w,h = 0,0
    for i in sizes:
        i.sort()
        if w < i[0]:
            w = i[0]
        if h < i[1]:
            h = i[1]
    answer = w * h
    return answer