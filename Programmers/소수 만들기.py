import itertools

def is_prime(num):
    temp = int(num ** 0.5)
    for i in range(2, temp + 1):
        if num % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    comb  = list(itertools.combinations(nums,3))
    case_list = []
    
    for i in comb:
        case_list.append(sum(i))
    for i in case_list:
        answer += is_prime(i)
    return answer