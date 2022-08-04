def solution(id_list, report, k):
    answer = []
    zeros = [0 for _ in range(len(id_list))]
    report = list(set(report))
    new_id_list = dict(zip(id_list, zeros))
    answer_list = dict(zip(id_list, zeros))
    for i in report:
        temp = list(i.split())
        new_id_list[temp[1]] += 1
    for i in report:
        temp = list(i.split())
        if new_id_list[temp[1]] >= k:
            answer_list[temp[0]] += 1
    for v in answer_list.values():
        answer.append(v)
    return answer