n = int(input())

a = n // 5

answer_case = []

for i in range(a + 1):
    temp = n - (5 * i)

    if temp % 3 == 0:
        answer_case.append(i + (temp // 3))

if len(answer_case) == 0:
    print(-1)
else:
    print(min(answer_case))
