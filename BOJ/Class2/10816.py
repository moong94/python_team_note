from collections import Counter

n = int(input())
n_card = list(map(int,input().split()))

counter = Counter(n_card)
m = int(input())
m_card = list(map(int,input().split()))

for i in m_card:
    print(counter[i], end=" ")