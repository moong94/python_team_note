import sys

n = int(sys.stdin.readline())

s = set()
for _ in range(n):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        command[1] = set([int(command[1])])

    if command[0] == "add":
        s = s | command[1]
    elif command[0] == "remove":
        s -= command[1]
    elif command[0] == "check":
        if command[1] & s:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] & s:
            s -= command[1]
        else:
            s = s | command[1]
    elif command[0] == "all":
        s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif command[0] == "empty":
        s = set()


