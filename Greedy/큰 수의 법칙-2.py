n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

# 값이 더해지는 횟수를 통해 답을 구하는 것
# 시간 복잡도를 더 많이 줄일 수 있음

count1 = (m // (k + 1)) * k
count1 += m % (k + 1)

count2 = m - count1

answer = (data[0] * count1) + (data[1] * count2)

print(answer)