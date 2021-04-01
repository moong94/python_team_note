n, m = map(int,input().split())
k = list(map(int,input().split()))

answer = 0

k.sort()

count = 1

for i in range(n - 1):
    if k[i] == k[i + 1]:
        count += 1
        continue
    answer += ((n - (i + 1)) * count)
    count = 1

print(answer)