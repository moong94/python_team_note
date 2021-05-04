k = int(input())

dp = [[0] * 2 for _ in range(k + 1)]

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, k + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

print(dp[k][0])
print(dp[k][1])