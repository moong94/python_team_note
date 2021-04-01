s = str(input())

answer = 0

count_0 = 0
count_1 = 0

if s[0] == "1":
    count_0 += 1
else:
    count_1 += 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        continue
    else:
        if s[i + 1] == "1":
            count_0 += 1
        else:
            count_1 += 1

print(min(count_1,count_0))
