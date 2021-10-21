def solution(price, money, count):
    answer = 0
    sum_price = ((count * (count + 1)) / 2) * price
    sum_price -= money
    if sum_price >= 0:
        return sum_price
    return answer