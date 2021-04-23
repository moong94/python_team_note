n = int(input())

t_li = []
p_li = []

dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    t, p = map(int,input().split())
    t_li.append(t)
    p_li.append(p)

for i in range(n - 1, -1, -1):
    time = t_li[i] + i

    if time <= n:
        dp[i] = max(p_li[i] + dp[time], max_value)
        max_value = dp[i]

    else:
        dp[i] = max_value


print(max_value)