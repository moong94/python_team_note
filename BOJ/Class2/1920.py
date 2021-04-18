n = int(input())
a = set(map(int,input().split()))

m = int(input())
data = list(map(int,input().split()))

for i in data:
    if i in a:
        print("1")
    else:
        print("0")