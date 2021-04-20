import sys

n = int(sys.stdin.readline())

member = []
for _ in range(n):
    inform = sys.stdin.readline().split()
    member.append((int(inform[0]), inform[1]))

member.sort(key = lambda x: x[0])

for a,n in member:
    print(a,n)