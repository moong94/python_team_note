n = int(input())

data = []

ranking =[]

for _ in range(n):
    w, h  = map(int,input().split())
    data.append((w,h))

for i in range(n):
    rank = 1
    for j in range(n):
        if data[j][0] > data[i][0] and data[j][1] > data[i][1]:
            rank += 1

    ranking.append(rank)

for i in ranking:
    print(i, end=" ")