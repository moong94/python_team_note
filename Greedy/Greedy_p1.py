n = 1260
count = 0

coin_type = [500,100,50,10]

for i in coin_type:
    count += n // i
    n %= i

print(count)