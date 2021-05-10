import sys

input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    start, end = map(int,input().split())
    li.append((start,end))

li.sort(key = lambda x: x[0])
li.sort(key = lambda x: x[1])

tmp = 0
count = 0
for i in li:
    if i[0] >= tmp:
        count += 1
        tmp = i[1]

print(count)