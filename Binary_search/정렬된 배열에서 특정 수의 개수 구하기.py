n , x = map(int,input().split())
data = list(map(int,input().split()))

start = 0
end = len(data)

def first(array, start, end, target):
    while start <= end:
        mid = (end + start) // 2
        if array[mid] == target:
            end = mid - 1
            mid = end
        elif array[mid] < target:
            start = mid + 1
    return mid

def last(array, start, end, target):
    while start <= end:
        mid = (end + start) // 2

        if array[mid] == target:
            start = mid + 1
            mid = start
        elif array[mid] > target:
            end = mid - 1

    return mid

def binary_search(array, start, end, target):
    while start < end:
        mid = (end + start) // 2
        if array[mid] == target:
            f_num = first(array, start, mid - 1, target)
            l_num = last(array, mid + 1, end, target)
            return l_num - f_num - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(binary_search(data, 0, n - 1, x))



