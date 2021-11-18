def solution(n, times):
    answer = 0
    start, end = 0, max(times) * n
    
    while start < end:
        mid = (start + end) // 2
        can_n = 0
        for i in times:
            can_n += mid // i
            if can_n >= n:
                break
        
        if can_n >= n:
            end = mid
            answer = mid
        else:
            start = mid + 1
    return answer