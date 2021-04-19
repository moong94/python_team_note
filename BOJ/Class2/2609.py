n, m = map(int,input().split())

def gcd(n,m):
    if n % m == 0:
        return m

    n, m = m, n % m
    return gcd(n,m)


gcd_num= gcd(n, m)

lcm_num = gcd_num * (n // gcd_num) * (m // gcd_num)

print(gcd_num)
print(lcm_num)