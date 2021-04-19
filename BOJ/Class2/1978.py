n = int(input())

data = list(map(int,input().split()))

number = [False, False] + [True] * (max(data) - 1)

for i in range(2, int((len(number) - 1) ** 0.5) + 1):
    if number[i] == False:
        continue
    for j in range(i + i, len(number),i):
        number[j] = False

count = 0
for i in data:
    if number[i] == True:
        count += 1

print(count)