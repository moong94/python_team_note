def solution(s):
    answer = ''
    s = list(map(int,s.split()))
    s.sort()
    answer = str(s[0]) + " " + str(s[-1])
    return answer