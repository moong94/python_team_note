import sys

k = int(sys.stdin.readline())
li = []

for _ in range(k):
    num = int(sys.stdin.readline())

    if num == 0:
        li.pop()
    else:
        li.append(num)

if len(li) == 0:
    print(0)
else:
    print(sum(li))
