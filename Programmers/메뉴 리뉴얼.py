from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        dict = {}
        for j in orders:
            comb = list(combinations(sorted(list(j)),i))
            for k in comb:
                temp = "".join(k)
                if temp in dict.keys():
                    dict[temp] += 1
                else:
                    dict[temp] = 1
        if dict:
            max_value = max(dict.values())
            if max_value == 1:
                continue
            for key,value in dict.items():
                if value == max_value:
                    answer.append(key)
    answer.sort()
    return answer