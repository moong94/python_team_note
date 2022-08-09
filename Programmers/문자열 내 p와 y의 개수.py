def solution(s):
    answer = True
    s = s.lower()
    s_cnt = s.count('p')
    y_cnt = s.count('y')
    
    if s_cnt == y_cnt:
        return True
    else:
        return False