import sys

input = sys.stdin.readline

n, m = map(int,input().split())

numbers = list(map(int,input().split()))

sum_numbers = [0] * (n + 1)

for i in range(1, n + 1):
    sum_numbers[i] = sum_numbers[i - 1] + numbers[i - 1]

for _ in range(m):
    start, end = map(int,input().split())

    print(sum_numbers[end] - sum_numbers[start - 1])
