from itertools import permutations

def case(case_x, k, dungeons):
    temp = 0
    for i in case_x:
        if k >= dungeons[i][0]:
            k -= dungeons[i][1]
            temp += 1
    return temp

def solution(k, dungeons):
    answer = -1
    len_d = len(dungeons)
    li = [i for i in range(len_d)]
    perm = list(permutations(li,len_d))
    
    for i in perm:
        i_case = case(i, k ,dungeons)
        if i_case > answer:
            answer = i_case
        
    return answer