n = int(input())

a = list(map(int,input().split()))

temp = [0] * n

temp[0] = 1

for i in range(1, n):
    init = 0
    for j in range(i):
        if a[i] > a[j]:
            init = max(init,temp[j])
    temp[i] = init + 1

print(max(temp))
