m, n = map(int,input().split())

data = [False, False] + [True] * (n - 1)

for i in range(2, int(n ** 0.5) + 1):
    if data[i]:
        for j in range(i + i,len(data), i):
            data[j] = False
for i in range(len(data)):
    if data[i] and i >= m:
        print(i)