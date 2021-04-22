n, m = map(int,input().split())

dp = [10001] * 10001

memo = []

for _ in range(n):
    num = int(input())
    dp[num] = 1
    memo.append(num)
for i in range(1,m + 1):
    for j in memo:
        if i == j:
            continue
        elif i - j > 0:
            dp[i] = min(dp[i],dp[i-j] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])