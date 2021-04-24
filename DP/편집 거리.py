a = input()
b = input()

dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]

dp_column = 1
for i in b:
    dp_row = 1
    for j in a:
        if i == j:
            dp[dp_column][dp_row] = dp[dp_column - 1][dp_row - 1] + 1
        else:
            dp[dp_column][dp_row] = max(dp[dp_column - 1][dp_row], dp[dp_column][dp_row - 1])

        dp_row += 1
    dp_column += 1

print(len(a) + len(b) - (2 * dp[-1][-1]) - 1)
