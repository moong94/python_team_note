from itertools import permutations

n, m = map(int,input().split())

temp = list(map(int,input().split()))

arr = list(set(permutations(temp,m)))
arr.sort()
for i in arr:
    for j in i:
        print(j, end=" ")
    print()