import heapq
import sys

input = sys.stdin.readline

t = int(input())

def test_case(k):
    min_heap = []
    max_heap = []
    visited = [False] * 1000001
    arr = []
    for i in range(k):
        oper, n = map(str,input().split())
        n = int(n)
        if oper == "D":
            if n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif n == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
        if oper == "I":
            arr.append(n)
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (n * -1, i))
            visited[i] = True
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if max_heap and min_heap:
        print(max_heap[0][0] * -1, min_heap[0][0])
    else:
        print("EMPTY")


for _ in range(t):
    k = int(input())
    test_case(k)