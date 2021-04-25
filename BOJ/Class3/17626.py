n = int(input())

dp = [4] * (n + 1)

dp[0], dp[1] = 0, 1

for i in range(1, int(n ** 0.5) + 1):
    dp[i ** 2] = 1

for i in range(2, n + 1):
    if dp[i] == 1:
        continue
    for j in range(1, int(i ** 0.5)):
        dp[i] = min(dp[i], dp[j ** 2] + dp[i - (j ** 2)])

print(dp[n])