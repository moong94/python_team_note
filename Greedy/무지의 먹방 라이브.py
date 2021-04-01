def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food = []
    for i in range(len(food_times)):
        food.append([food_times[i], i + 1])

    food = sorted(food, key=lambda x: x[0], reverse=True)

    next_previous = 0
    previous = 0
    sum_value = 1
    while (k - (sum_value * len(food))) > 0:
        previous = food[-1][0] - next_previous
        next_previous += previous
        k -= previous * len(food)
        if k < 0:
            k += previous * len(food)
            break
        food.pop()
        if len(food) == 0:
            break
        sum_value = food[-1][0] - next_previous

    food = sorted(food, key=lambda x: x[1])
    return food[k % len(food)][1]