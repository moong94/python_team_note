n = int(input())

storage = list(map(int,input().split()))

m = int(input())

guest = list(map(int,input().split()))

for i in range(m):
    if guest[i] in storage:
        print("yes", end = " ")
    else:
        print("no", end=" ")