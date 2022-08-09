import itertools

def solution(numbers):
    answer = set([])
    temp = list(itertools.permutations(numbers,2))
    
    for i in temp:
        answer.add(sum(i))
    answer = list(answer)
    answer.sort()
    return answer