n = int(input())
move = list(map(str,input().split()))

now = [1,1]

for i in move:
    if i == "L" and now[1] != 1:
        now[1] -= 1
    elif i == "R" and now[1] != n:
        now[1] += 1
    elif i == "U" and now[0] != 1:
        now[0] -= 1
    elif i == "D" and now[0] != n:
        now[0] += 1

print(now[0],now[1])