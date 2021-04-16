n = int(input())

data = [int(input()) for _ in range(n)]
list = [i for i in range(n, 0, -1)]
stack = []
answer = []

y_n = 0

for temp in data:
    if len(stack) != 0 and stack[-1] == temp:
        stack.pop()
        answer.append("-")
        continue
    else:
        if len(list) != 0 and list[-1] <= temp:
            while True:
                stack.append(list.pop())
                answer.append("+")
                if stack[-1] == temp:
                    stack.pop()
                    answer.append("-")
                    break
        else:
            y_n = 1
            break

if y_n == 1:
    print("NO")
else:
    print("\n".join(answer))