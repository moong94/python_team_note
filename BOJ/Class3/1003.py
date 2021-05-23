import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    fibonacci = [0,1]
    for i in range(n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    if n == 0:
        print(1, 0)
    else:
        print(fibonacci[-3], fibonacci[-2])
