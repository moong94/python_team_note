import sys
input = sys.stdin.readline

n = int(input())

papers = [list(map(int,input().split())) for _ in range(n)]

white = 0
blue = 0

def cut(x,y,n):
    global white, blue
    check = papers[x][y]
    for i in range(x,x + n):
        for j in range(y,y + n):
            if papers[i][j] != check:
                for a in range(2):
                    for b in range(2):
                        cut(x + n // 2 * a, y + n // 2 * b, n //2)
                return
    if check == 1:
        blue += 1
    elif check == 0:
        white += 1
cut(0,0,n)

print(white)
print(blue)
