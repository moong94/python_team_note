def solution(s):
    answer = [0,0]
    while s != "1":
        s_count = s.count("0")
        answer[1] += s_count
        answer[0] += 1
        new_s_len = len(s) - s_count
        s = bin(new_s_len)[2:]
    return answer