while True:
    num = input()

    if num == '0':
        break
    r_num = num[::-1]

    if num == r_num:
        print("yes")
    else:
        print("no")
