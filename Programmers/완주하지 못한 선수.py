def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if len(answer) == 0:
        answer = participant[-1]
    
    return answer