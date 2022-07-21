def solution(passes, minutes, result):
    # [기본요금, 기본 시간, 추가 시간 간격, 추가 요금]
    
    answer = 0
    
    result_list = []
    for bp, bt, it, ap in passes:
        minute = minutes
        charge = bp
        minute -= bt
        if minute > 0:
            charge += (minute // it) * ap
            if minute % it != 0:
                charge += ap
        result_list.append(charge)
    
    answer = min(result_list)

    return answer

print(solution([[5000,120,20,1000],[3000,30,20,3000]], 150, 7000))
print(solution([[24500,1000,1,0],[7000,10,50,3000],[9000,60,20,2000]], 180, 19000))
print(solution([[5000,100,1,50],[8000,200,1,25],[2500,25,1,100]], 10, 2500))