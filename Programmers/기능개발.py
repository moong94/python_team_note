def solution(progresses, speeds):
    answer = []
    idx = 0
    while idx < len(progresses):
        for i in range(idx, len(progresses)):
            progresses[i] += speeds[i]
        temp = 0
        while progresses[idx] >= 100:
            temp += 1
            idx += 1
            if idx >= len(progresses):
                break
        if temp != 0:
            answer.append(temp)
                
    return answer