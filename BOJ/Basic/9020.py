T = int(input())

ex_list = []
for i in range(T):
    ex_list.append(int(input()))

max_num = max(ex_list)

prime_list = [False, False] + [True for _ in range(max_num - 1)]

for i in range(2, max_num + 1):
    if prime_list[i]:
        for j in range(i * 2, max_num + 1, i):
            prime_list[j] = False

for i in ex_list:
    a, b = i // 2, i // 2
    while True:
        if prime_list[a] and prime_list[b]:
            print("%d %d"%(a,b))
            break
        else:
            a -= 1
            b += 1