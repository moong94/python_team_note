from itertools import permutations
import re

def solution(expression):
    answer = 0
    perm = list(permutations(["+","-","*"]))
    numbers = re.split('[*+-]', expression)
    operators = re.split("[0-9]+", expression)
    
    new_expression = []
    
    for i in range(len(numbers)):
        new_expression.append(numbers[i])
        new_expression.append(operators[i + 1])
    op_case = new_expression[:-1]
    
    for case in perm:
        case_x = op_case[:]
        temp = []
        for i in case:
            idx = 0
            while idx < len(case_x):
                if case_x[idx] == i:
                    if i == "+":
                        temp.append(int(temp.pop()) + int(case_x[idx + 1]))
                    elif i == "-":
                        temp.append(int(temp.pop()) - int(case_x[idx + 1]))
                    elif i == "*":
                        temp.append(int(temp.pop()) * int(case_x[idx + 1]))
                    idx += 1
                else:
                    temp.append(case_x[idx])
                idx += 1
            case_x = temp
            temp = []
        if abs(case_x[0]) > answer:
            answer = abs(case_x[0])
    return answer