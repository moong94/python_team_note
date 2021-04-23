n = int(input())

soldier = list(map(int,input().split()))

soldier.reverse()

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    max_num = 0
    for j in range(i):
        if soldier[i] > soldier[j]:
            max_num = max(max_num, dp[j])
    dp[i] = max_num + 1

print(n - max(dp))