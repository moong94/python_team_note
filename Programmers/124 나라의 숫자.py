def solution(n) : 
    answer = ''
    while n > 2:
        temp = n % 3
        if temp == 0:
            answer = '4' + answer
            n //= 3
            n -= 1
        else:
            answer = str(temp) + answer
            n //= 3
    if n != 0:
        answer = str(n) + answer
    return answer