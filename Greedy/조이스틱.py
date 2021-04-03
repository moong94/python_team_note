def solution(name):
    answer = 0

    length = len(name)
    init = ["A"] * length

    now = 0
    name = list(map(str, name))

    while True:
        if name == init:
            return answer

        r_count = 0
        l_count = 0

        r = now
        l = now
        while name[r] == "A":
            r += 1
            if r == length:
                r_count += 1
                r = 0
        while name[l] == "A":
            l -= 1
            if l == -length - 1:
                l_count += 1
                l = -1

        if abs(now - (r + (r_count * length))) <= abs(now - (l - (l_count * length))):
            move = r
        else:
            move = l
        answer += abs(now - move)
        now = move

        if ord(name[now]) <= 78:
            answer += ord(name[now]) - 65
        else:
            answer += 91 - ord(name[now])
        name[now] = "A"

    return answer