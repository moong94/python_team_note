from itertools import count

num_list = []
while True:
    n = int(input())
    if n == 0:
        break
    num_list.append(n)

max_num = max(num_list)
prime_list = [False, False] + [True for _ in range(max_num * 2 - 1)]

for i in range(2, 2 * max_num  + 1):
    if prime_list[i]:
        for j in range(i * 2, len(prime_list), i):
            prime_list[j] = False

for i in range(len(num_list)):
    print(prime_list[num_list[i] + 1:num_list[i] * 2 + 1].count(True))