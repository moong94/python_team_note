import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

s = input()

i = 1
count = 0
answer = 0

while i < m - 1:
    if s[i - 1 : i + 2] == "IOI":
        count += 1
        if count == n:
            answer += 1
            count -= 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)