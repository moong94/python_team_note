n = int(input())
l = input()

answer = 0

for i in range(n):
    answer += (ord(l[i]) - ord('a') + 1) * (31 ** i)

print(answer % 1234567891)