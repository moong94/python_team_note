import sys
from collections import Counter

n = int(sys.stdin.readline())
number_list = []

for i in range(n):
    number_list.append(int(sys.stdin.readline()))

number_list.sort()

number_count = Counter(number_list).most_common()

# 산술평균
print(round(sum(number_list) / n))

# 중앙 값
print(number_list[n // 2])

# 최빈값
if len(number_count) > 1:
    if number_count[0][1] == number_count[1][1]:
        print(number_count[1][0])
    else:
        print(number_count[0][0])
else:
    print(number_count[0][0])

# 범위
print(number_list[-1] - number_list[0])