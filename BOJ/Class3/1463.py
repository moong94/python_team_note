import sys
input = sys.stdin.readline

x = int(input())

dp = [0] * (x + 1)

if x < 2:
    dp[0], dp[1] = 0,0
elif x < 3:
    dp[0], dp[1],dp[2] = 0,0,1
else:
    dp[0],dp[1],dp[2],dp[3] = 0,0,1,1

for i in range(4,x + 1):
    ex = []
    if i % 2 == 0:
        ex.append(dp[i // 2])
    if i % 3 == 0:
        ex.append(dp[i // 3])
    ex.append(dp[i - 1])

    dp[i] = min(ex) + 1

    
print(dp[x])
