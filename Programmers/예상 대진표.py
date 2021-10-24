import math

def recur(n,a,b,cnt):
    if a <= n // 2 and b <= n // 2:
        return recur(n // 2, a, b, cnt - 1)
    elif a > n // 2 and b > n // 2:
        return recur(n // 2, a - (n // 2), b - (n // 2), cnt - 1)
    else:
        return cnt
    
def solution(n,a,b):
    answer = math.log2(n)
    
    answer = recur(n, a, b, answer)
    
    return answer