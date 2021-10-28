def solution(record):
    answer = []
    result_dict = {}
    result_list = []
    for i in record:
        temp = i.split()
        
        cmd, uid = temp[0], temp[1]
        if cmd == "Enter":
            result_dict[uid] = temp[2]
            result_list.append((uid,0))
        elif cmd == "Leave":
            result_list.append((uid,1))
        elif cmd == "Change":
            result_dict[uid] = temp[2]
            
    for i in result_list:
        if i[1] == 0:
            answer.append(result_dict[i[0]] + "님이 들어왔습니다.")
        elif i[1] == 1:
            answer.append(result_dict[i[0]] + "님이 나갔습니다.")
    return answer