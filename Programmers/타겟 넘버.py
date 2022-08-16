answer = 0

def dfs(idx, result, numbers, target):
    if idx == len(numbers):
        if result == target:
            global answer
            answer += 1
        return
    dfs(idx + 1, result + numbers[idx], numbers, target)
    dfs(idx + 1, result - numbers[idx], numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer