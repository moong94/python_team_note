n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

answer = 0

i = 0

while True:
    for _ in range(k):
        if m == i:
            break

        answer += data[0]
        print(answer)
        i += 1

    if m == i:
        break
    answer += data[1]
    i += 1

print(answer)

