rest = []


for i in range(10):
    data = (int(input()))
    rest.append(data % 42)


rest = list(set(rest))

print(len(rest))