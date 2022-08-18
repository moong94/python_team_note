def solution(priorities, location):
    answer = 0
    dict_priorities = dict()
    idx = 9
    new_priorities = list(zip([i for i in range(len(priorities))],priorities))
    for i in priorities:
        if i in dict_priorities:
            dict_priorities[i] += 1
        else:
            dict_priorities[i] = 1
    while new_priorities:
        if idx not in dict_priorities:
            idx -= 1
            continue
        if dict_priorities[idx] == 0:
            idx -= 1
            continue
        if dict_priorities[idx] > 0:
            if new_priorities[0][1] != idx:
                new_priorities.append(new_priorities.pop(0))
            else:
                dict_priorities[idx] -= 1
                tmp = new_priorities.pop(0)
                answer += 1
                if tmp[0] == location:
                    return answer  