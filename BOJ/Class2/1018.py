n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(input()))

answer_case = []

def count(array):
    answer1 = 0
    answer2 = 0
    for i in range(8):
        for j in range(8):
            if ((i + j) % 2 == 0 and array[i][j] != "W") or ((i + j) % 2 == 1 and array[i][j] != "B"):
                answer1 += 1
            else:
                answer2 += 1

    return min(answer1,answer2)


for i in range(n - 7):
    temp = [[0] * 8 for _ in range(8)]
    for j in range(m - 7):

        for k in range(8):
            for l in range(8):
                temp[k][l] = data [i + k][j + l]

        answer_case.append(count(temp))

print(min(answer_case))