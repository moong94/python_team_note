import sys

n, m, b = map(int,sys.stdin.readline().split())

land = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

answer_case = []

for test_case in range(257):

    time = 0
    block = b
    for i in range(n):
        for j in range(m):
            if land[i][j] < test_case:
                block -= test_case - land[i][j]
                time += test_case - land[i][j]
            elif land[i][j] > test_case:
                block += land[i][j] - test_case
                time += ((land[i][j] - test_case) * 2)


    if block < 0:
        break
    else:
        answer_case.append((time, test_case))
answer_case.sort(key=lambda x: -x[0])

print(answer_case[-1][0], answer_case[-1][1])
