def solution(math_scores, english_scores):
    answer = 0

    math_rank = [[k,i] for i, k in enumerate(math_scores)]
    math_rank.sort(key=lambda x:x[0])
    english_rank = [[k,i] for i, k in enumerate(english_scores)]
    english_rank.sort(key=lambda x:x[0])
    
    rankings = [[0,0] for _ in range(len(math_scores))]

    for i in range(len(math_scores)):
        rankings[math_rank[i][1]][0] += len(math_scores) - i
        rankings[english_rank[i][1]][1] += len(english_scores) - i

    for i in range(len(rankings)):
        for j in range(i + 1, len(rankings)):
            if rankings[i][0] > rankings[j][0] and rankings[i][1] > rankings[j][1]:
                answer += 1
            elif rankings[i][0] < rankings[j][0] and rankings[i][1] < rankings[j][1]:
                answer += 1
    return answer

print(solution([70, 65, 90, 80, 50],[40, 20, 30, 60, 50]))
print(solution([90,91,95,99,100], [20,40,60,80,100]))
print(solution([80,50,30,20,10],[24,39,47,63,75]))