import sys

input = sys.stdin.readline

n = int(input())

answer = ""

arr = list(map(int,input().split()))
sorted_arr = sorted(set(arr))

dict = {sorted_arr[i] : i for i in range(len(sorted_arr))}

for i in arr:
    print(dict[i], end = " ")
