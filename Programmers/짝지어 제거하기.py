def solution(s):
    stack = []
    
    for i in range(len(s)):
        if stack:
            if stack[-1] != s[i]:
                stack.append(s[i])
            else:
                stack.pop()
        else:
            stack.append(str(s[i]))
    if stack:
        return 0
    return 1