import sys
input = sys.stdin.readline

n,m = map(int,input().split())

l_list = []
h_list = []
answer = []

for _ in range(n):
    l_list.append(input().rstrip())
for _ in range(m):
    h_list.append(input().rstrip())

l_list.sort()
h_list.sort()

i = 0
j = 0

while i < n and j < m:
    if l_list[i] == h_list[j]:
        answer.append(l_list[i])
        i += 1
        j += 1
    elif l_list[i] < h_list[j]:
        i += 1
    else:
        j += 1

print(len(answer))
print("\n".join(answer))
