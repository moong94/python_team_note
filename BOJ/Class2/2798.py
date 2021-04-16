from itertools import combinations

n, m = map(int,input().split())

card= list(map(int,input().split()))

answer_list = []

picks = list(combinations(card,3))

for i in picks:
    answer_list.append(sum(i))

answer = 0

for i in answer_list:
    if i <= m and i> answer:
        answer = i

print(answer)
