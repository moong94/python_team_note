data = []

for i in range(9):
    data.append(int(input()))

max_num = max(data)

print(max_num)
print(data.index(max_num) + 1)