primes = [False, False] + [True for _ in range(1000001 - 2)]
for i in range(2, len(primes)):
    if primes[i]:
        for j in range(i * 2, len(primes), i):
            primes[j] = False
def solution(n):
    answer = primes[1 : n + 1].count(True)
    return answer