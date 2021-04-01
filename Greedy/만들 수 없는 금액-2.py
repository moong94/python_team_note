n = int(input())
data = list(map(int, input().split()))

answer = 1

data.sort()

for i in data:
    if answer < i:
        break
    else:
        answer += i

print(answer)