def to_lower_bite(num, count):
    for i in range(count):
        num *= 1024
    return num

def solution(units, numbers):
    answer = 0
    byte_list = ['B','KB','MB','GB','TB']
    temp_list = [_ for _ in range(5)]
    
    byte_dict = dict(zip(byte_list,temp_list))
    print(byte_dict)
    for i in range(len(units)):
        answer += to_lower_bite(numbers[i], byte_dict[units[i]])
    return answer

print(solution(["B","KB","MB","GB","TB"],[1234567890123,455221625,770988,96,2]))