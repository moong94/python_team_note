def solution(n):
    answer = 0
    temp = ''
    while n > 2:
        temp = str(n % 3) + temp
        n //= 3
    temp = str(n) + temp
    temp = list(temp)
    for i in range(len(temp)):
        answer += int(temp[i]) * (3 ** i)
    return answer