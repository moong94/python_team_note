n = int(input())
solutions = list(map(int,input().split()))

start = 0
end = n - 1

answer = []

answer_start_case = start
answer_end_case = end

init = solutions[start] + solutions[end]
min_result = init

while start < end:
    result = solutions[start] + solutions[end]
    min_result = min(abs(result),abs(min_result))

    if min_result == abs(result):
        answer_start_case = start
        answer_end_case = end

    if result == 0:
        break
    elif result > 0:
        end -= 1
    else:
        start += 1

print(solutions[answer_start_case], solutions[answer_end_case])