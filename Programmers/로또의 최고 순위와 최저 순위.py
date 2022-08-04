def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    correct_count = 0
    for i in lottos:
        if i == 0:
            zero_count += 1
        elif i in win_nums:
            correct_count += 1
    max_rank = 7 - (correct_count + zero_count)
    min_rank = 7 - correct_count
    if max_rank >= 7:
        max_rank = 6
    if min_rank >= 7:
        min_rank = 6
    answer = [max_rank, min_rank]
    return answer