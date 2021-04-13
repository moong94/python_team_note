n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

for _ in range(k):
    a = array_a.index(min(array_a))
    b = array_b.index(max(array_b))
    if min(array_a) < max(array_b):
        array_a[a], array_b[b] = array_b[b], array_a[a]
    else:
        break

print(sum(array_a))