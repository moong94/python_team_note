def solution(n):
    temp = 2
    while True:
        if n % temp == 1:
            return temp
        temp += 1