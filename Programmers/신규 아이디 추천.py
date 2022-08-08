def solution(new_id):
    answer = ''
    # 1
    answer = new_id.lower()
    
    # 2
    temp = ''
    for i in answer:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            temp += i
    answer = temp
    
    print(answer)
    #3
    temp = ''
    for i in answer:
        if i == '.':
            if len(temp) != 0 and temp[-1] == '.':
                continue
        temp += i
    answer = temp
    
    # 4
    answer = answer.strip('.')
    
    # 5
    if len(answer) == 0:
        answer = 'a'
    
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        answer = answer.rstrip('.')
        
    # 7
    if len(answer) < 3:
        while(len(answer) < 3):
            answer += answer[-1]
        
    return answer