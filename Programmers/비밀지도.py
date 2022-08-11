def solution(n, arr1, arr2):
    new_map = []
    new_list = []
    for i in range(n):
        new_map.append(arr1[i] | arr2[i])
        dec_to_hex = str(bin(arr1[i] | arr2[i]))[2:]
        new_list.append('0' * (n - len(dec_to_hex)) + dec_to_hex)   
    for i in range(n):
        new_list[i] = new_list[i].replace('1','#')
        new_list[i] = new_list[i].replace('0',' ')
            
    return new_list