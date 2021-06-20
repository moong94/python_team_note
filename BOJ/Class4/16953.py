a, b = map(int,input().split())

answer = 0

while True:
    if b % 10 == 1:
        b //= 10
        answer += 1
    elif b % 2 == 1:
        print(-1)
        break
    else:
        b //= 2
        answer += 1

    if b == a:
        answer += 1
        print(answer)
        break
    elif b < a:
        print(-1)
        break
