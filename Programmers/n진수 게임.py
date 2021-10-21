def n_notation(num, n):
    temp = ""
    li = "0123456789ABCDEF"
    while True:
        temp = li[num % n] + temp
        num //= n
        if num == 0:
            break
    return list(temp)

def solution(n, t, m, p):
    answer = ''
    cnt = 0
    temp = []
    num = 0
    while len(temp) < t * m + p - 1:
        temp += n_notation(num, n)
        num += 1
    for i in range(t):
        answer += temp[m * i + p - 1]
    return answer