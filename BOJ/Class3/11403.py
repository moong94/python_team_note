n = int(input())
visited = [0 for i in range(n)]
s = []
def dfs(v):
    for i in range(n):
        if visited[i] == 0 and s[v][i] == 1:
            visited[i] = 1
            dfs(i)

for i in range(n):
    s.append(list(map(int,input().split())))

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

    visited = [0 for i in range(n)]