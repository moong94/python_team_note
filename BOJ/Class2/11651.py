import sys

n = int(sys.stdin.readline())

data = []

for _ in range(n):
    x, y = sys.stdin.readline().split()
    data.append((int(x),int(y)))

data.sort(key = lambda x: (x[1],x[0]))

for x,y in data:
    print(x,y)