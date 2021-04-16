data = list(map(int,input().split()))

a = 0
d = 0

for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        a += 1
    elif data[i] > data[i + 1]:
        d += 1

if a != 0 and d != 0:
    print("mixed")
elif a == 0:
    print("descending")
else:
    print("ascending")