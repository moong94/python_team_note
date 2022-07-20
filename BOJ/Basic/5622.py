import sys

word = sys.stdin.readline().strip()

dial = {}

temp = 0

answer = 0

for i in range(5):
    for j in range(3):
        dial[chr(ord('A') + temp)] = i + 3
        temp += 1

for i in range(4):
    dial[chr(ord('A') + temp)] = 8
    temp += 1

for i in range(3):
    dial[chr(ord('A') + temp)] = 9
    temp += 1

for i in range(4):
    dial[chr(ord('A') + temp)] = 10
    temp += 1

for i in word:
    answer += dial[i]

print(answer)