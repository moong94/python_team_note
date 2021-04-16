n = int(input())
data = set()
for _ in range(n):
    data.add(input())

data = list(data)
data.sort()
data.sort(key=lambda x:len(x))

for i in data:
    print(i)