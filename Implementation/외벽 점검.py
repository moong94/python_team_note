from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1

    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)

    for start in range(length):
        for i in list(permutations(dist, len(dist))):
            count = 1

            position = weak[start] + i[count - 1]

            for j in range(start, start + length):
                if position < weak[j]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[j] + i[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1

    return answer