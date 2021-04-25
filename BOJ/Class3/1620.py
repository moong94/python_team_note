import sys

n , m = map(int,sys.stdin.readline().split())
poketmon_dict = {}
poketmon_list = []


for i in range(n):
    x = sys.stdin.readline().rstrip()
    poketmon_dict[x] = i + 1
    poketmon_list.append(x)

for _ in range(m):
    quiz = sys.stdin.readline().rstrip()

    if quiz.isalpha():
        print(poketmon_dict[quiz])
    else:
        print(poketmon_list[int(quiz) - 1])