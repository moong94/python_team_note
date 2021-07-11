import heapq

t = int(input())

def test_case(k):
    min_heap = []
    max_heap = []

    arr = []
    for _ in range(k):
        oper, n = map(str,input().split())
        n = int(n)
        if oper == "D":
            if arr:
                arr.pop()
                if n == -1:
                    heapq.heappop(min_heap)
                elif n == 1:
                    heapq.heappop(max_heap)
            else:
                continue
        if oper == "I":
            arr.append(n)
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap,n * -1)
    if arr:
        print(heapq.heappop(max_heap) * -1, heapq.heappop(min_heap))
    else:
        print("EMPTY")


for _ in range(t):
    k = int(input())
    test_case(k)