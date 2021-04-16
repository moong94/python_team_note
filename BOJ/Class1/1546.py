n = int(input())

score = list(map(int,input().split()))

m = max(score)

total = 0

for i in score:
    total += (i / m) * 100

print(total / n)

