import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    dictionary = dict()
    for _ in range(n):
        val, key = map(str,input().split())

        if key in dictionary.keys():
            dictionary[key] += 1
        else:
            dictionary[key] = 1

    answer = 1
    for i in dictionary.values():
        answer *= (i + 1)

    print(answer - 1)