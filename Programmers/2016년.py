def solution(a, b):
    answer = ''
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    weekdays = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = 0
    day += sum(days[:a - 1])
    day += b - 1
    answer = weekdays[day % 7]
    return answer