N = int(input())

answer = 0
answer_list = []
def move(start, to):
    global answer
    answer += 1
    answer_list.append(start + " " + to)

def hanoi(N, start, to, via):
    if N == 1:
        move(start, to)
    else:
        hanoi(N - 1, start, via, to)
        move(start, to)
        hanoi(N - 1, via, to, start)

hanoi(N, '1', '3', '2')
print(answer)
for i in answer_list:
    print(i)