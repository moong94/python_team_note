from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    
    queue = deque(people)
    while len(queue) > 1:
        temp = queue[-1]
        i = 0
        while True:
            
            if temp <= limit:
                temp += queue[i]
                i += 1
            else:
                queue.pop()
                for _ in range(i - 1):
                    queue.popleft()
                answer += 1
                break
    if queue:
        answer += 1
    return answer