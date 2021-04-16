k, n = map(int,input().split())

data = []
for _ in range(k):
    data.append(int(input()))

start = 0
end = max(data)
count = 0

answer = []

while start <= end:
    mid = (start + end) // 2
    answer_case = 0
    for i in data:
        answer_case += i // mid

    if answer_case >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)