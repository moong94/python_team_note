def product(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in product(arr, n - 1):
                yield [arr[i]] + next

arr = [1,2,3,4,5]

print(list(product(arr, 3)))