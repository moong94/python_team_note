import sys

N = int(sys.stdin.readline())

answer = 0

for i in range(N):
    word_list = list(sys.stdin.readline().strip())

    if len(word_list) == 1:
        answer += 1
        continue

    zipped_word = ""
    zipped_word += word_list[0]
    for j in range(1, len(word_list)):
        if word_list[j] != zipped_word[-1]:
            zipped_word += word_list[j]
    
    word_set = set(word_list)
    
    if len(zipped_word) == len(word_set):
        answer += 1

print(answer)