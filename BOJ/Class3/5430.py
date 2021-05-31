import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    command = input()
    n = int(input())
    x = input()
    list_x = x[1:-2].split(",")
    left, right, reverse = 0, 0, 0
    for i in command:
        if i == "R":
            reverse += 1
        elif i == "D":
            if reverse % 2 == 0:
                left += 1
            else:
                right += 1
    if left + right > n:
        print("error")
    else:
        if reverse % 2 == 0:
            tmp = ",".join(list_x[left: -(right + 1)])
        else:
            tmp = ",".join(list_x[left: -(right + 1):-1])
        print("[" + tmp + "]")
        print(left,-(right + 1))
