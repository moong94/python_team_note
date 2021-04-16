s = input()

s = list(s.upper())

temp = []

for i in s:
    if i not in temp:
        temp.append(i)

count = [0] * len(temp)
j = 0
for i in temp:
    count[j] += s.count(i)
    j += 1

if count.count(max(count)) >= 2:
    print("?")
else:
    print(temp[count.index(max(count))])

