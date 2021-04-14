n, m = map(int,input().split())

cakes = list(map(int,input().split()))

def binary_search(cakes, start, end, target):
    answer = 0

    while (start <= end):
        mid = (start + end) // 2
        sum = 0
        for i in range(len(cakes)):
            if cakes[i] >= mid:
                sum += cakes[i] - mid
        if sum < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer

print(binary_search(cakes,0,max(cakes), m))