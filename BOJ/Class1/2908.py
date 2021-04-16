num1, num2 = map(str,input().split())

num1_list = list(num1)
num2_list = list(num2)

num1_list.reverse()
num2_list.reverse()

for i in range(3):
    if num1_list[i] > num2_list[i]:
        print("".join(num1_list))
        break
    elif num2_list[i] > num1_list[i]:
        print("".join(num2_list))
        break
