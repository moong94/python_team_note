import sys

n = int(sys.stdin.readline())

data = [0 for _ in range(10001)]

for _ in range(n):
    data[int(sys.stdin.readline())] += 1


for i in range(len(data)):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)