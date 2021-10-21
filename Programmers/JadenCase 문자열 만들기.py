def solution(s):
    answer = ''
    s_list = s.split(" ")
    for i in range(len(s_list)):
        if len(s_list[i]) == 0:
            continue
        s_list[i] = s_list[i][0].upper() + s_list[i][1:].lower()
    answer = " ".join(s_list)
    
    return answer