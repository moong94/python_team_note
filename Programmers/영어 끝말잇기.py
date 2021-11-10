def solution(n, words):
    answer = [0,0]
    used_word = {}
    last_str = ""
    turn = 0
    for i in range(len(words)):
        if words[i] in used_word.keys():
            turn = i
            break
        if i != 0 and last_str != words[i][0]:
            turn = i
            break
        last_str = words[i][-1]
        used_word[words[i]] = 1
    if turn:
        answer = [turn % n + 1, (turn // n) + 1]
    return answer