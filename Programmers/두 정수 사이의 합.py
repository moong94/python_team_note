def solution(a, b):
    if a > b:
        a, b = b, a
    answer = ((a + b) * ((b - a) + 1)) // 2
    return answer