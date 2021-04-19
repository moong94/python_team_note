while True:
    bracket = []

    opt = -1

    string = input()
    if string == ".":
        break

    for i in string:
        if i == "(":
            bracket.append(i)
        elif i == "[":
            bracket.append(i)
        elif i == ")":
            if len(bracket) != 0 and bracket[-1] == "(":
                bracket.pop()
            else:
                print("no")
                break
        elif i == "]":
            if len(bracket) != 0 and bracket[-1] == "[":
                bracket.pop()
            else:
                print("no")
                break
        if i == ".":
            if len(bracket) == 0:
                print("yes")
            else:
                print("no")

