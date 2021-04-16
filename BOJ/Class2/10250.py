t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    answer = 0
    if n % h == 0:
        answer += h * 100
        answer += n // h
    else:
        answer += (n % h) * 100
        answer += (n // h + 1)

    print(answer)