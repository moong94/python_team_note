string = input()

numbers = list(map(str,string.split("-")))

for i in range(len(numbers)):
    tmp = list(map(int,numbers[i].split("+")))
    numbers[i] = sum(tmp)

    if i != 0:
        numbers[i] *= -1

print(sum(numbers))
