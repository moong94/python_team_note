import sys

n ,x = map(int,input().split())

data = list(map(int,input().split()))

for i in data:
    if i < x:
        print(i, end=" ")