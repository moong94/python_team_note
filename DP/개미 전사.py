n = int(input())

storage = list(map(int,input().split()))

dp = [0] * 101

dp[0] = storage[0]
dp[1] = max(storage[0], storage[1])

for i in range(2,n):
    dp[i] = max(dp[i - 1], dp[i - 2] + storage[i])

print(dp)
print(dp[n - 1])