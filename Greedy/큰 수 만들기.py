def solution(number, k):
    answer = ''

    lenght = len(number)

    i = 1
    while k > 0:
        if i == len(number):
            break
        if number[i - 1] < number[i]:
            number = number[:i - 1] + number[i:]
            if i != 1:
                i -= 1
            k -= 1
            continue
        i += 1

    while len(number) > lenght - k:
        number = number[:-1]

    return number