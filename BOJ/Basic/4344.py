import sys

C = int(input())

for i in range(C):
    std_list = list(map(int, input().split()))
    avg = sum(std_list[1:]) / std_list[0]
    count = 0
    for j in range(len(std_list) - 1):
        if std_list[j + 1] > avg:
            count += 1
    print("{0:.3f}%".format(count / std_list[0] * 100))