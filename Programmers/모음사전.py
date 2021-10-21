from itertools import product

def solution(word):
    answer = 0
    aeiou = ["A","E","I","O","U"]
    temp_list = []
    temp = []
    for i in range(1,6):
        temp_list.append(list(product(aeiou,repeat=i)))
    for i in temp_list:
        for j in i:
            s = "".join(j)
            temp.append(s)
    temp.sort()
    answer = temp.index(word) + 1
    return answer