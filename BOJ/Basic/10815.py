N = int(input())
N = [i for i in range(N)]
N_list = list(map(int, input().split()))
N_list = list(zip(N_list, N))
N_list.sort(key = lambda x:x[0])

M = int(input())
M = [i for i in range(M)]
M_list = list(map(int, input().split()))
M_list = list(zip(M_list, M))
M_list.sort(key = lambda x:x[0])

answer_list = [0 for _ in range(len(M))]
start_n = 0
start_m = 0
while True:
    if start_n >= len(N_list) or start_m >= len(M_list):
        break
    if M_list[start_m][0] == N_list[start_n][0]:
        answer_list[M_list[start_m][1]] = 1
        start_m += 1
        start_n += 1
    elif M_list[start_m][0] > N_list[start_n][0]:
        start_n += 1
    else:
        start_m += 1


print(" ".join(map(str,answer_list)))