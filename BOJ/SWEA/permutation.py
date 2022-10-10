def permutation(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i] + arr[i+1:], n - 1):
                yield [arr[i]] + next

arr = [1,2,3,4,5]

print(list(permutation(arr, 3)))