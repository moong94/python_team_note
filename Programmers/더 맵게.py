import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        temp = heapq.heappop(scoville)
        if temp >= K:
            break
        heapq.heappush(scoville, temp + heapq.heappop(scoville) * 2)
        answer += 1
    if heapq.heappop(scoville) < K:
        return -1
    return answer