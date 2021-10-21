def gcd(a,b):
    max_num, min_num = max(a,b), min(a,b)
    new_a, new_b = min_num, max_num % min_num
    if new_b == 0:
        return new_a
    return gcd(new_a,new_b)

def lcm(a,b,gcd):
    return a * b // gcd

def solution(arr):
    answer = 0
    for i in range(len(arr) - 1):
        arr[i + 1] = lcm(arr[i], arr[i + 1], gcd(arr[i],arr[i + 1]))
    
    answer = arr[-1]
    
    return answer