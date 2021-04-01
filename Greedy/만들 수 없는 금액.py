from itertools import combinations

n = int(input())
coin = list(map(int, input().split()))

answer = 0

x = []


for i in range(n):
    x.append(list(combinations(coin, i + 1)))

sum_x = []

for i in range(n):
    for j in range(len(x[i])):
        sum_x.append(sum(x[i][j]))

for i in range(1, max(sum_x)):
    if i in sum_x:
        continue
    else:
        answer = i
        break;

if answer == 0:
    answer = max(sum_x) + 1

print(answer)
