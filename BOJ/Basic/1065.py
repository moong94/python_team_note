import sys

N = int(sys.stdin.readline())

answer = 0

def sequence(li):
    num_diff = int(li[0]) - int(li[1])
    for i in range(1, len(li) - 1):
        if int(li[i]) - int(li[i + 1]) != num_diff:
            return 0
    return 1

for i in range(1, N + 1):
    temp_list = list(str(i))
    if len(temp_list) == 1 or len(temp_list) == 2:
        answer += 1
        continue
    else:
        answer += sequence(temp_list)

print(answer)