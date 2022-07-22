X = int(input())

i = 1
temp = 0
while temp < X:
    temp += i
    i += 1

need = X - temp + i - 2

if i % 2 == 1:
    start_c = 1 + need
    start_p = i - 1 - need
else:
    start_c = i - 1 - need
    start_p = 1 + need

print("%d/%d"%(start_c, start_p))
