from itertools import combinations

n, m = map(int,input().split())

li = list(i for i in range(1,n + 1))

comb = list(combinations(li, m))

for i in comb:
    for j in i:
        print(j,end=" ")
    print()