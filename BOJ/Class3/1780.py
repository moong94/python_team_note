import sys

input = sys.stdin.readline

n = int(input())

minus = 0
zero = 0
plus = 0

papers = [list(map(int,input().split())) for _ in range(n)]


def cut(x,y,n):
    global minus, zero, plus
    check = papers[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if papers[i][j] != check:
                for a in range(3):
                    for b in range(3):
                        cut(x + n // 3 * a, y + n // 3 * b, n // 3)
                return
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    elif check == 1:
        plus += 1

cut(0,0,n)

print(minus)
print(zero)
print(plus)