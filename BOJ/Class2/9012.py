n = int(input())

for _ in range(n):
    string = input()

    temp = []

    for i in string:
        if i == "(":
            temp.append(i)
        else:
            if len(temp) != 0 and temp[-1] == "(":
                temp.pop()
            else:
                temp.append(i)
                break

    if len(temp) == 0:
        print("YES")
    else:
        print("NO")