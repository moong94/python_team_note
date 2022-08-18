import itertools

def solution(numbers):
    numbers = sorted(numbers, key=lambda x: str(x) * 3, reverse = True)
    answer = ''
    for i in numbers:
        answer += str(i)
    return str(int(answer))