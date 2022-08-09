def cases(li, answers):
    answer = 0
    for i in range(len(answers)):
        if answers[i] == li[i % len(li)]:
            answer += 1
    return answer

def solution(answers):
    answer = []
    case_1 = [1,2,3,4,5]
    answer_1 = 0
    case_2 = [2,1,2,3,2,4,2,5]
    amswer_2 = 0
    case_3 = [3,3,1,1,2,2,4,4,5,5]
    answer_3 = 0
    
    answer_1 = cases(case_1, answers)
    answer_2 = cases(case_2, answers)
    answer_3 = cases(case_3, answers)
    
    max_rank = max(answer_1, answer_2, answer_3)
    
    if answer_1 == max_rank:
        answer.append(1)
    if answer_2 == max_rank:
        answer.append(2)
    if answer_3 == max_rank:
        answer.append(3)
    
    return answer