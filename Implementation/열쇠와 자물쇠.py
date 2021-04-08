def rotate(arr_lock):
    n = len(arr_lock)
    m = len(arr_lock[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = arr_lock[i][j]
    return result


def check(arr_lock):
    mid = len(arr_lock) // 3

    for i in range(mid, mid * 2):
        for j in range(mid, mid * 2):
            if arr_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(key)
    m = len(lock)

    new_lock = [[0] * 3 * m for _ in range(m * 3)]
    for i in range(m, 2 * m):
        for j in range(m, 2 * m):
            new_lock[i][j] = lock[i - m][j - m]

    for _ in range(4):
        key = rotate(key)
        for i in range(2 * m):
            for j in range(2 * m):
                for k in range(n):
                    for l in range(n):
                        new_lock[i + k][j + l] += key[k][l]

                if check(new_lock) == True:
                    return True

                for x in range(n):
                    for y in range(n):
                        new_lock[i + x][j + y] -= key[x][y]

    return False