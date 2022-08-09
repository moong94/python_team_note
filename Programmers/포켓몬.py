def solution(nums):
    answer = 0
    n = len(nums) // 2
    nums = set(nums)
    cnt = len(nums)
    
    if cnt < n:
        answer = cnt
    else:
        answer = n
        
    return answer