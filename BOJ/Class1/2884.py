h, m = map(int,input().split())

m = m - 45

if m < 0:
    h = h - 1
    m = 60 + m
    if h < 0:
        h = 23

print(h, m)