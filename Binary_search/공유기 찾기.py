n, c = map(int,input().split())

x_list = []
for _ in range(n):
    x_list.append(int(input()))

x_list.sort()

start = 1
end = x_list[-1] - x_list[0]

answer = 0

while start <= end:
    mid = (start + end) // 2
    value = x_list[0]
    count = 1

    for i in range(1, n):
        if x_list[i] >= value + mid:
            value = x_list[i]
            count += 1
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)
