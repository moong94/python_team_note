t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    mine = list(map(int,input().split()))

    dp = [0] * (n * m)

    for i in range(n):
        dp[i * m] = mine[i * m]

    for i in range(1, m):
        for j in range(n):
            now = mine[m * j + i]
            if (j - 1) * m + i - 1 < 0:
                dp[(m * j) + i] = max(dp[(m * j) + i - 1] + now, dp[(m * (j + 1)) + i - 1] + now)
            elif (j + 1) * m + i - 1 >= n * m:
                dp[(m * j) + i] = max(dp[(m * j) + i - 1] + now, dp[(m * (j - 1)) + i - 1] + now)
            else:
                dp[(m * j) + i] = max(dp[(m * j) + i - 1] + now, dp[(m * (j - 1)) + i - 1] + now, dp[(m * (j + 1)) + i - 1] + now)
    print(max(dp))
