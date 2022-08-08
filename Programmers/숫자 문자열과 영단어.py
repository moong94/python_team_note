def solution(s):
    number_list = [str(i) for i in range(10)]
    char_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
    dict_num = list(zip(char_list, number_list))
    
    for i in range(10):
        s = s.replace(dict_num[i][0], dict_num[i][1])
    
    answer = int(s)
    return answer