a = int(input())
b = int(input())
c = int(input())

data = a * b * c

data = list(map(int,str(data)))

for i in range(10):
    print(data.count(i))


