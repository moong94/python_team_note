N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

answer_list = []
for i in M_list:
    if i in N_list:
        N_list.remove(i)
        answer_list.append('1')
    else:
        answer_list.append('0')

print(" ".join(answer_list))