def combination_with_replacement(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in combination_with_replacement(arr[i:], n - 1):
                yield [arr[i]] + next

arr = [1,2,3,4,5]

print(list(combination_with_replacement(arr, 3)))