n = int(input())

answer = 0

for i in range(n, 0, -1):
    li = list(map(int,str(i)))
    if i + sum(li) == n:
        answer = i

print(answer)