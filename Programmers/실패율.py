def solution(N, stages):
    answer = []
    players = len(stages)
    result_list = [i for i in range(1,N + 1)]
    failure_list = []
    stages.sort()
    
    for i in range(1, N + 1):
        cnt = 0
        for j in range(len(stages)):
            if stages[j] == i:
                cnt += 1
                if j == len(stages) - 1:
                    failure_list.append(cnt / len(stages))
            else:
                failure_list.append(cnt / len(stages))
                stages = stages[j:]
                break
    result_list = list(zip(result_list, failure_list))
    result_list.sort(key = lambda x:x[1], reverse=True)
    print(result_list)
    for i, j in result_list:
        answer.append(i)
    return answer