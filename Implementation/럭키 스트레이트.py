n = str(input())

left = [int(n[i]) for i in range(len(n) // 2)]
right = [int(n[i]) for i in range(len(n) // 2, len(n))]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")