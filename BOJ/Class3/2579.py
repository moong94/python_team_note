import sys

input = sys.stdin.readline

n = int(input())

dp = [[[0,0],[0,0]] for _ in range(n + 1)]

stairs = []

stairs.append(0)

for _ in range(n):
    stairs.append(int(input()))


dp[1][0][0], dp[1][0][1], dp[1][1][0], dp[1][1][1] = stairs[1], 1, stairs[1], 2

for i in range(2,len(stairs)):
    dp[i][0][0], dp[i][0][1] = max(dp[i - 2][0][0], dp[i - 2][1][0]) + stairs[i], 1
    dp[i][1][0], dp[i][1][1] = dp[i - 1][0][0] + stairs[i], 2

print(max(dp[-1][0][0], dp[-1][1][0]))

