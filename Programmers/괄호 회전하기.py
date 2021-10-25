from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        brackets = []
        for j in s:
            if not brackets:
                brackets.append(j)
                continue
            if j ==")":
                if brackets[-1] == "(":
                    brackets.pop()
            elif j == "]":
                if brackets[-1] == "[":
                    brackets.pop()
            elif j == "}":
                if brackets[-1] == "{":
                    brackets.pop()
            else:
                brackets.append(j)
        if not brackets:
            answer += 1
        s.append(s.popleft())
    return answer