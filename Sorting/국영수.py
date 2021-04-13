n = int(input())

student = []
for _ in range(n):
    name, score1,score2,score3 = map(str,input().split())
    student.append((name,int(score1),int(score2),int(score3)))

student.sort(key=lambda x:x[0])
student.sort(key=lambda x:x[3], reverse=True)
student.sort(key=lambda x:x[2])
student.sort(key=lambda x:x[1], reverse=True)

for i in range(n):
    print(student[i][0])