from dataclasses import replace


N = int(input())

stars = [['0'] * N for _ in range(N)]
def recursive(n):
    global stars
    if n == 3:
        stars[0][0:3] = ['1','1','1']
        stars[1][0:3] = ['1','0','1']
        stars[2][0:3] = ['1','1','1']
        return
    recursive(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(n // 3):
                stars[n // 3 * i + k][n // 3 * j : n // 3 * (j + 1)] = stars[k][:n // 3]

recursive(N)
print(stars)
for i in stars:
    print("".join(i).replace("1","*").replace("0"," "))