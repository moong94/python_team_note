N = int(input())

answer = 1

def factorial(num):
    global answer
    if num == 0:
        answer *= 1
        return
    answer *= num
    factorial(num - 1)

factorial(N)
print(answer)

