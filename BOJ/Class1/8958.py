n = int(input())

data = []

for i in range(n):
    data.append(input())


for i in data:
    answer = 0
    score = 0
    for j in range(len(i)):
        if i[j] == "O":
            score += 1
            answer += score
        elif i[j] == "X":
            score = 0
    print(answer)