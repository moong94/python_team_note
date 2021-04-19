import sys

n = int(sys.stdin.readline())
number = []
for _ in range(n):
    number.append(int(sys.stdin.readline()))

number.sort()

for i in number:
    print(i)