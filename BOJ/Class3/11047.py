n, k = map(int,input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

count = 0
while k > 0:
    for i in coins:
        count += k // i
        k %= i

print(count)