from bisect import bisect_left, bisect_right


def count(a, left, right):
    right_idx = bisect_right(a, right)
    left_idx = bisect_left(a, left)

    return right_idx - left_idx


array = [[] for _ in range(10001)]

reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != "?":
            res = count(array[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        else:
            res = count(reversed_array[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z"))
        answer.append(res)

    return answer