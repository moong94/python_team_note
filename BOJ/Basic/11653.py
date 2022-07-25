N = int(input())

i = 2
r = int(N ** 0.5)
while i <= r:
    if N % i == 0:
        print(i)
        N //= i 
        if N == 1:
            break
        continue
    i += 1
if N > 1:
    print(N)