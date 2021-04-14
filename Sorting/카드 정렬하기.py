import heapq

n = int(input())

heap = []

for _ in range(n):
    data = int(input())
    heapq.heappush(heap,data)

answer = 0

while len(heap) != 1:

    first = heapq.heappop(heap)
    second = heapq.heappop(heap)

    sum_value = first + second
    answer += sum_value
    heapq.heappush(heap, sum_value)

print(answer)


