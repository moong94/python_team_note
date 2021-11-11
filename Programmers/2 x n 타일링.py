def solution(n):
    answer = 0
    dp_0 = 1
    dp_1 = 2
    for i in range(2, n):
        dp_2 = dp_0 + dp_1
        dp_0, dp_1 = dp_1, dp_2
    answer = dp_2 % 1000000007
    return answer