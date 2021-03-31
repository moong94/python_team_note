n, m = map(int, input().split())

answer = 0

for _ in range(n):
    card = list(map(int,input().split()))
    min_number = min(card)

    answer = max(min_number, answer)

print(answer)