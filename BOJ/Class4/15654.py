from itertools import permutations

n, m = map(int,input().split())
numbers = list(map(int,input().split()))

numbers.sort()

per = list(permutations(numbers,m))

for i in per:
    for j in i:
        print(j, end=" ")
    print()
