t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    floor = [[0] * (n + 1) for i in range(k + 1)]

    for i in range(n + 1):
        floor[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            floor[i][j] = floor[i - 1][j] + floor[i][j - 1]

    print(floor[k][n])