def solution(dartResult):
    answer = 0
    new_list = []
    temp = ''
    for i in list(dartResult):
        if i.isdigit():
            temp += i
        else:
            if temp:
                new_list.append(temp)
            new_list.append(i)
            temp = ''
    temp = 0
    result_list = []
    for i in new_list:
        if i.isdigit():
            result_list.append(int(i))
        elif i == 'S':
            continue
        elif i == 'D':
            result_list[-1] **= 2
        elif i == 'T':
            result_list[-1] **= 3
        elif i == '#':
            result_list[-1] *= -1
        elif i == '*':
            if len(result_list) > 1:
                result_list[-1] *= 2
                result_list[-2] *= 2
            else:
                result_list[-1] *= 2
    answer = sum(result_list)
    return answer