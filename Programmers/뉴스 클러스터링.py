def make_set(li):
    temp = []
    for i in range(len(li) - 1):
        if (li[i] >= "a" and li[i] <= "z") or (li[i] >= "A" and li[i] <= "Z"):
            if (li[i + 1] >= "a" and li[i + 1] <= "z") or (li[i + 1] >= "A" and li[i + 1] <= "Z"):
                temp.append(li[i].upper() + li[i + 1].upper())
    return temp

def make_intersection(str1, str2):
    cnt = 0
    temp = [False] * len(str2)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if not temp[j]:
                    temp[j] = True
                    cnt += 1
                    break
    return cnt
    
def solution(str1, str2):
    answer = 0
     
    set_li_str1 = make_set(str1)
    set_li_str2 = make_set(str2)
    
    intersection = make_intersection(set_li_str1, set_li_str2)
    union = len(set_li_str1) + len(set_li_str2) - intersection
    
    if union == 0:
        return 65536
    answer = intersection / union * 65536
    return int(answer)