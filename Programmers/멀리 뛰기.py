def solution(n):
    dp = [0 for _ in range(n)]
    dp[0] = 1
    if n > 1:
        dp[1] = 2
    
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    answer = dp[-1] % 1234567
    return answer