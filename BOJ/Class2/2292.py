n = int(input())

answer = 1
n -= 1
while True:
    if n <= 0:
        break
    n -= 6 * answer
    answer += 1

print(answer)