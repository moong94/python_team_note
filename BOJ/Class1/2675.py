t = int(input())

data = []

for _ in range(t):
    r, s = map(str,input().split())
    data.append((int(r),s))

for i in data:
    for j in range(len(i[1])):
        print(i[1][j] * i[0], end="")
    print()
