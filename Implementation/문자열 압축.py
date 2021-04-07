def solution(s):
    answer = len(s)
    length = 1

    for i in range(1, len(s) // 2 + 1):
        string = ""
        previous = s[0:i]
        count = 1

        for j in range(i, len(s), i):
            if previous == s[j:j + i]:
                count += 1
            else:
                string += str(count) + previous if count >= 2 else previous
                previous = s[j:j + i]
                count = 1
        string += str(count) + previous if count >= 2 else previous

        answer = min(answer, len(string))

    return answer