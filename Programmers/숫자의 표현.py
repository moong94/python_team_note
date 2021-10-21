def solution(n):
    answer = 0
    li = [i for i in range(1,n + 1)]
    start = 0
    end = 0
    while start < len(li) and end < len(li):
        temp = sum(li[start:end + 1])
        if temp == n:
            answer += 1
            end += 1
        elif temp > n:
            start += 1
        else:
            end += 1
    return answer