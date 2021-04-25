import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dict = {}

for _ in range(n):
    site, pwd = map(str,input().split())
    dict[site] = pwd

for _ in range(m):
    find = input().rstrip()
    print(dict[find])