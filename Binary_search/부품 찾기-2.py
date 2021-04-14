n = int(input())

storage = list(map(int,input().split()))

m = int(input())

guest = list(map(int,input().split()))

storage.sort()

def binary_search(array,start,end,target):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in range(m):
    if binary_search(storage, 0, n - 1, guest[i]):
        print("yes", end=" ")
    else:
        print("no", end=" ")
