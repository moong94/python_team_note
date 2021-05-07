n = int(input())

mid = (n + 1) // 2

answer = 1

for i in range(n - 1, mid - 1, -1):
    temp = 1
    for j in range(n - i):
        temp *= (i - j)
        temp //= (j + 1)
    temp *= (2 ** (j + 1))
    answer += temp

print(answer % 10007)