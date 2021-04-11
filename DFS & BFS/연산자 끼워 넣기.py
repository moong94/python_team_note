from itertools import permutations

n = int(input())
a = list(map(int,input().split()))
op_ex = ["+", "-", "*", "%"]

operations = list(map(int,input().split()))

op = []

for i in range(4):
    for j in range(operations[i]):
      op.append(op_ex[i])

case = list(set(permutations(op)))

answer_case = []
for i in case:
    temp = a[0]
    for j in range(len(i)):
        if i[j] == "+":
            temp += a[j + 1]
        elif i[j] == "-":
            temp -= a[j + 1]
        elif i[j] == "*":
            temp *= a[j + 1]
        elif i[j] == "%":
            if temp < 0:
                temp *= -1
                temp //= a[j + 1]
                temp *= -1
            else:
                temp //= a[j + 1]
    answer_case.append(temp)

print(max(answer_case))
print(min(answer_case))


