def solution(numbers):
    answer = []
    for i in numbers:
        temp = ""
        if i % 2 == 0:
            answer.append(i + 1)
        else:
            for j in range(len(bin(i)) - 1, 1, -1):
                if bin(i)[j] == "0":
                    temp = bin(i)[:j] + "10" + bin(i)[j + 2:]
                    break
            if not temp:
                temp ="0b10" + bin(i)[3:]
            answer.append(int(temp,2))
    return answer