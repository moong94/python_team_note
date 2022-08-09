def solution(d, budget):
    answer = 0
    total = 0
    d.sort()

    for i in range(len(d)):
        total += d[i]
        if total > budget:
            break
        answer += 1
    return answer