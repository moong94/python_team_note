n = int(input())

data = list(map(int,input().split()))

start = 0
end = len(data) - 1

while start <= end:
    mid = (start + end) // 2

    if data[mid] == mid:
        print(mid)
        break
    elif data[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1

if start > end:
    print(-1)