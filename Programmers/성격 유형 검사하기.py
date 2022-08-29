def solution(survey, choices):
    answer = ''
    score_list = [0,3,2,1,0,1,2,3]
    personality = ["R","T","C","F","J","M","A","N"]
    temp = [0] * 8
    personality_dict = dict(zip(personality,temp))
    
    for i in range(len(survey)):
        if choices[i] < 4:
            personality_dict[list(survey[i])[0]] += score_list[choices[i]]
        else:
            personality_dict[list(survey[i])[1]] += score_list[choices[i]]
    
    for i in range(0,8,2):
        if personality_dict[personality[i]] >= personality_dict[personality[i + 1]]:
            answer += personality[i]
        else:
            answer += personality[i + 1]
    
    return answer