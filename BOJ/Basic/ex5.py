def solution(taxes, income):
    answer = 0
    idx = len(taxes) - 1        
    for i in range(len(taxes) - 1):
        if income <= taxes[i][0]:
            idx = i             
            break

    for i in range(idx):
        if i == 0:
            answer += taxes[0][0] * (taxes[0][1] / 100)
        else:
            answer += (taxes[i][0] - taxes[i - 1][0]) * (taxes[i][1] / 100)
        
    
    answer += (income - taxes[idx - 1][0]) * (taxes[idx][1] / 100)
   
    return int(answer)

print(solution([[1200, 6], [4600, 15], [8800, 24], [15000, 35], [0, 38]], 9500))
print(solution([[1000, 1], [0, 10]], 2000))
print(solution([[1500, 12], [3500, 23], [5700, 29], [0, 30]], 6400))