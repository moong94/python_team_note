n = int(input())

li = [0] * n
li[0] = 1

idx2 = idx3 = idx5 = 0

next2, next3, next5 = 2,3,5

for i in range(1,n):
    li[i] = min(next2,next3,next5)

    if li[i] == next2:
        idx2 += 1
        next2 = li[idx2] * 2
    if li[i] == next3:
        idx3 += 1
        next3 = li[idx3] * 3
    if li[i] == next5:
        idx5 += 1
        next5 = li[idx5] * 5


print(li[n - 1])