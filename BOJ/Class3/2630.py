import sys
input = sys.stdin.readline

n = int(input())

papers = [list(map(int,input().split())) for _ in range(n)]

white = 0
blue = 0

def cut(x,y,n):
    global blue,white
    check = papers[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != papers[i][j]:
                cut(x,y,n // 2)
                cut(x,y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return

    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

cut(0,0,n)
print(white)
print(blue)