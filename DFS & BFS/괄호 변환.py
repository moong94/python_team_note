def solution(p):
    answer = ''

    # 1
    if p == "":
        return p

    u, v = balance(p)

    # 3
    if right(u):
        answer += u + solution(v)
    # 4
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = u[1:-1]
        u = list(u)
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            elif u[i] == ")":
                u[i] = "("
        answer += "".join(u)
    return answer


# 3
def right(u):
    count = 0
    for i in range(len(u)):
        if u[i] == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            return False
    return True


# 2
def balance(w):
    count = 0
    for i in range(0, len(w)):
        if w[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            u = w[:i + 1]
            v = w[i + 1:]
            break

    return u, v