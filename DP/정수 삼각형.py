n = int(input())

data = []
dp = []
for i in range(n):
    data.append(list(map(int,input().split())))
    dp.append([0] * (i + 1))

dp[0][0] = data[0][0]

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + data[i][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + data[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j] + data[i][j], dp[i - 1][j - 1] + data[i][j])

print(max(dp[-1]))