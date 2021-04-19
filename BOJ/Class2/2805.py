n, m = map(int,input().split())

trees = list(map(int,input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2

    total = 0

    for i in trees:
        if i > mid:
            total += i - mid

    if total == m :
        end = mid
        break
    elif total < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)