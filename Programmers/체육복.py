def solution(n, lost, reserve):
    student = [0] + [1 for _ in range(n)] + [0]
    lost.sort()
    for i in lost:
        student[i] -= 1
    for i in reserve:
        student[i] += 1
    
    for i in lost:
        if student[i] == 0 and student[i - 1] == 2:
            student[i - 1] -= 1
            student[i] += 1
        elif student[i] == 0 and student[i + 1] == 2:
            student[i + 1] -= 1
            student[i] = 1
    answer = len(student) - student.count(0)
    return answer