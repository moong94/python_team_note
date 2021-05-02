import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 11

dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(n):
    t = int(input())
    print(dp[t])