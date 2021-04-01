n = int(input())
x = list(map(int, input().split()))

answer = 0

x.sort()

group = []

for i in x:
    group.append(i)
    if len(group) >= i:
        group = []
        answer += 1

print(answer)