import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

temp_list = [False, False] + ([True] * (N - 1))

for i in range(2, N + 1):
    for j in range(2 * i, N + 1, i):
        temp_list[j] = False

answer = 0
least_num = -1
for i in range(M, N + 1):
    if temp_list[i] == True:
        answer += i
        if least_num == -1:
            least_num = i

if answer == 0:
    print(-1)
else:
    print(answer)
    print(least_num)    