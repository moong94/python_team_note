t = int(input())

dp = [0] * 101

dp[1:11] = [1,1,1,2,2,3,4,5,7,9]

test_case = [int(input()) for _ in range(t)]

max_num = max(test_case)

for i in range(11,max_num + 1):
    dp[i] = dp[i - 1] + dp[i - 5]

for i in test_case:
    print(dp[i])