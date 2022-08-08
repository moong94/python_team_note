def finger_select(l_point, r_point, points, hand):
    result = ''
    l = abs(l_point[0] - points[0]) + abs(l_point[1] - points[1])
    r = abs(r_point[0] - points[0]) + abs(r_point[1] - points[1])
    
    if l == r:
        if hand == "right":
            r_point = points
            result = 'R'
        else:
            l_point = points
            result = 'L'
    else:
        if l < r:
            l_point = points
            result = 'L'
        else:
            r_point = points
            result = 'R'
    return l_point, r_point, result

def solution(numbers, hand):
    answer = ''
    l_point = [3,0]
    r_point = [3,2]
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            l_point = [i // 3, 0]
        elif i in [3,6,9]:
            answer += 'R'
            r_point = [i // 3 - 1, 2]
        elif i == 0:
            l_point, r_point, temp = finger_select(l_point, r_point, [3, 1], hand)
            answer += temp
        else:
            l_point, r_point, temp = finger_select(l_point, r_point, [i // 3, 1], hand)
            answer += temp
    return answer