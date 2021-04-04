n = input()

now = list(map(str, n))

count = 8

answer_list = []

answer_list.append([ord(now[0]) + 1, int(now[1]) + 2])
answer_list.append([ord(now[0]) + 1, int(now[1]) - 2])
answer_list.append([ord(now[0]) - 1, int(now[1]) + 2])
answer_list.append([ord(now[0]) - 1, int(now[1]) - 2])
answer_list.append([ord(now[0]) + 2, int(now[1]) + 1])
answer_list.append([ord(now[0]) + 2, int(now[1]) - 1])
answer_list.append([ord(now[0]) - 2, int(now[1]) + 1])
answer_list.append([ord(now[0]) - 2, int(now[1]) - 1])

for i in answer_list:
    if i[0] < ord("a"):
        count -= 1
    elif i[0] > ord("h"):
        count -= 1
    elif i[1] < 1:
        count -= 1
    elif i[1] > 8:
        count -= 1

print(count)


