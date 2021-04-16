import sys

datas = sys.stdin.readlines()


for data in datas:
    a, b = map(int, data.split())
    print(a + b)